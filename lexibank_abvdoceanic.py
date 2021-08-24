import re
from pathlib import Path

from nameparser import HumanName
from clldutils.misc import slug
from pylexibank.providers import abvd
from pylexibank.util import progressbar
from pylexibank import FormSpec


def normalize_contributors(l):
    for key in ['checkedby', 'typedby']:
        l[key] = normalize_names(l[key])
    return l


def normalize_names(names):
    res = []
    if names:
        for name in re.split('\s+and\s+|\s*&\s*|,\s+|\s*\+\s*', names):
            name = {
                'Simon': 'Simon Greenhill',
                'D. Mead': 'David Mead',
                'Alex François': 'Alexandre François',
                'Dr Alex François': 'Alexandre François',
                'R. Blust': 'Robert Blust',
            }.get(name, name)
            name = HumanName(name.title())
            res.append('{0} {1}'.format(name.first or name.title, name.last).strip())
    return ' and '.join(res)


class Dataset(abvd.BVD):
    dir = Path(__file__).parent
    id = 'abvdoceanic'
    SECTION = 'austronesian'
    
    form_spec = FormSpec(
        brackets={"[": "]", "{": "}", "(": ")"},
        separators=";/,~",
        missing_data=('-', ),
        strip_inside_brackets=True,
        replacements=[
            (" ", "_"),
            ("Vb1", ""),
            (" +", ""),
            (".", ""),
            ("3AUG", ""),
            ("3U-AUG", ""),
            ("#NAME?", ""),
            ("1", ""),
            ("? ", ""),
            ("#a-k", ""),
            (" ̂ŋ"[1:], "ŋ"),
            (" ̃pur"[1:], ""), 
            ('"""', ""),
            ("mo ̂ne", "mo ne"),
            ]
    )

    def cmd_download(self, args):
        raise NotImplementedException("Manually place raw XML files in ./raw/")
    


    def cmd_makecldf(self, args):
        args.writer.add_sources(*self.etc_dir.read_bib())
        concepts = args.writer.add_concepts(
            id_factory=lambda c: c.id.split('-')[-1]+ '_' + slug(c.english),
            lookup_factory=lambda c: c['ID'].split('_')[0]
        )
        for wl in progressbar(self.iter_wordlists(args.log), desc="cldfify"):
            args.writer.add_language(
                    ID=slug(wl.language.name, lowercase=False),
                    Glottocode=wl.language.glottocode,
                    ISO639P3code=wl.language.iso,
                    Name=wl.language.name,
                    author=wl.language.author,
                    url=wl.url('language.php?id=%s' % wl.language.id),
                    typedby=wl.language.typedby,
                    checkedby=wl.language.checkedby,
                    notes=wl.language.notes,
                    #source=";".join(source)
            )

            for entry in wl.entries:
                if entry.name is None or len(entry.name) == 0:  # skip empty entries
                    continue  # pragma: no cover

                # skip entries marked as incorrect word form due to semantics
                # (x = probably, s = definitely)
                if entry.cognacy and entry.cognacy.lower() in ('s', 'x'):
                    continue  # pragma: no cover

                # handle concepts
                cid = concepts.get(entry.word_id)
                if not cid:
                    wl.dataset.unmapped.add_concept(ID=entry.word_id, Name=entry.word)
                    # add it if we don't have it.
                    args.writer.add_concept(ID=entry.word_id, Name=entry.word)
                    cid = entry.word_id

                # handle lexemes
                try:
                    lex = args.writer.add_forms_from_value(
                        Local_ID=entry.id,
                        Language_ID=slug(wl.language.name, lowercase=False),
                        Parameter_ID=cid,
                        Value=entry.name,
                        # set source to entry-level sources if they exist, otherwise use
                        # the language level source.
                        #Source=[entry.source] if entry.source else source,
                        Cognacy=entry.cognacy,
                        Comment=entry.comment or '',
                        Loan=True if entry.loan and len(entry.loan) else False,
                    )
                except:  # NOQA: E722; pragma: no cover
                    args.log.warning("ERROR with %r -- %r" % (entry.id, entry.name))
                    raise

                if lex:
                    for cognate_set_id in entry.cognates:
                        match = wl.dataset.cognate_pattern.match(cognate_set_id)
                        if not match:  # pragma: no cover
                            args.log.warning('Invalid cognateset ID for entry {0}: {1}'.format(
                                entry.id, cognate_set_id))
                        else:
                            # make global cognate set id
                            cs_id = "%s-%s" % (slug(entry.word), match.group('id'))

                            args.writer.add_cognate(
                                lexeme=lex[0],
                                Cognateset_ID=cs_id,
                                Doubt=bool(match.group('doubt')),
                                Source=['Greenhilletal2008'] if wl.section == 'austronesian' else []
                            )

            #wl.to_cldf(args.writer, concepts)
            # Now normalize the typedby and checkedby values:
            args.writer.objects['LanguageTable'][-1] = normalize_contributors(args.writer.objects['LanguageTable'][-1])