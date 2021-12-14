"""
    Utility command for verifying generated phoneme inventories
    Isaac, Wed 17 Nov 2021
"""
from pathlib import Path

from cltoolkit import Wordlist
from pycldf import Dataset
from pyclts import CLTS
from tabulate import tabulate
from cldfcatalog import Config
from pyglottolog import Glottolog

from cldfbench.cli_util import with_dataset, get_dataset


def languages_for_family(glottolog, glottocode):
    """Return all languages and dialects descended from GLOTTOCODE, as
there seems to be no quick way of getting both language and dialect
descendants in pyglottolog - closest candidate seems to be
descendants_from_nodemap, but this method seems to only accept one
level at a time. Mattis?"""
    fam = glottolog.languoid(glottocode)
    # Walk the tree, collecting languages and dialects
    queue = [fam]
    output = []
    while queue:
        this = queue.pop()
        if this.level.id in ["dialect", "language"]:
            output.append(this)
        queue.extend(this.children)
    return output


def register(parser):
    parser.add_argument(
        "--family",
        help="Glottocode of subgroup to check alignments for",
    )
    parser.add_argument(
        "--output",
        default="inventories.tsv",
        help="Name of file to save inventory data in",
    )


def run(args):
    # Initialise Glottolog access
    cfg = Config.from_file()
    glottolog = Glottolog(cfg.get_clone("glottolog"))

    # Load data
    path = (Path(__file__).parents[1]).joinpath("cldf/cldf-metadata.json")
    bipa = CLTS().bipa
    wl = Wordlist([ Dataset.from_metadata(path) ], ts=bipa)

    languoids = languages_for_family(glottolog, args.family)

    family_codes = [lg.glottocode for lg in languoids]
    family_names = [lg.name for lg in languoids]

    rows = []
    for language in wl.languages:
        if language.glottocode in family_codes:
            # NB The language names in ABVD and Glottolog are different
            rows.append([
                language.name,
                language.glottocode,
                "https://glottolog.org/resource/languoid/id/{}".format(language.glottocode),
                len(language.sound_inventory.vowels),
                len(language.sound_inventory.consonants),
                " ".join([s.grapheme for s in language.sound_inventory.vowels]),
                " ".join([s.grapheme for s in language.sound_inventory.consonants]),
            ])
    args.log.info(
        "Found {} languages and dialects " \
        "in abvdoceanic under {}".format(len(rows), args.family)
    )

    table = tabulate(
        rows,
        headers=[
            "Name", "Glottocode", "Link", "# Vowels", "# Consonants",
            "Generated vowel phonemes", "Generated consonant phonemes"
        ],
        tablefmt="tsv",
    )

    with open(args.output, "w") as f:
        f.write(table)
        args.log.info("Inventory data for languages under {} written to {}".format(args.family, args.output))

    # Find orthography profiles in /etc matching languages in the given family
    # etcpath = Path(__file__).parent.joinpath("/etc")
    # orthprofiles = []
    # for p in etcpath.iterdir():
    #     if p.is_file() and p.stem in family_names:
    #         orthprofiles.append(p)

    # args.log.info(orthprofiles)
