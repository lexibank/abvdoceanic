"""
Calculate structural data from the wordlists in CLDF.
"""
from cldfbench.dataset import Dataset as BaseDataset
from pathlib import Path
from pylexibank import progressbar
import unicodedata
from unidecode import unidecode
from cltoolkit import Wordlist
from cltoolkit.util import iter_syllables
from pycldf import Dataset as PycldfDataset
from statistics import mean
from pyclts import CLTS
from pylexibank.cli_util import add_catalogs, add_dataset_spec

from cldfbench.cli_util import with_dataset, get_dataset
from cldfbench.datadir import DataDir
from pycldf.terms import Terms
from cldfbench import CLDFSpec
from clldutils.misc import slug

def register(parser):
    add_dataset_spec(parser)
    add_catalogs(parser, with_clts=True)


def compute_id(text):
    """
    Returns a codepoint representation to an Unicode string.
    """

    unicode_repr = "".join(["u{0:0{1}X}".format(ord(char), 4) for char in text])

    label = slug(unidecode(text))

    return "%s_%s" % (label, unicode_repr)


class StructureDataset(BaseDataset):
    dir = Path(__file__).parent
    id = "abvdoceanics"

    def __init__(self, directory):
        self.dir = DataDir(directory)
        self.metadata = self.metadata_cls()
        self.metadata.id = self.id

    def cldf_specs(self):
        return CLDFSpec(
                module='StructureDataset',
                dir=self.dir / 'cldf-structure',
                data_fnames={'ParameterTable': 'features.csv'}
            )
        
    def cmd_makecldf(self, args):
        
        wl = Wordlist(
                [PycldfDataset.from_metadata(self.dir / "cldf" / "cldf-metadata.json")],
                ts=args.clts.api.bipa)
        args.log.info("loaded data") 

        languages, values = [], []
        counter = 1
        segments = []
        for language in progressbar(wl.languages, desc="adding languages"):
            languaged = {
                    "ID": language.id,
                    "Name": language.name,
                    "Forms": len(language.forms),
                    "FormsWithSounds": len(language.forms_with_sounds),
                    "Concepts": len(language.concepts),
                    "Glottocode": language.glottocode,
                    "Latitude": language.latitude,
                    "Longitude": language.longitude,
                    "Family": language.family,
                    "Consonants": len(language.sound_inventory.consonants),
                    "ConsonantsByQuality": len(
                        language.sound_inventory.consonants_by_quality),
                    "ConsonantSounds": len(language.sound_inventory.consonant_sounds),
                    "Vowels": len(language.sound_inventory.vowels),
                    "VowelsByQuality": len(language.sound_inventory.vowels_by_quality),
                    "VowelSounds": len(language.sound_inventory.vowel_sounds)
                    }
            wlens, slens = [], []
            for form in language.forms_with_sounds:
                wlens += [len(form.sounds)]
                slens += [len(list(iter_syllables(form)))]
            languaged["WordLength"] = mean(wlens)
            languaged["SyllableLength"] = mean(slens)
            languages += [languaged]
            for sound in language.sound_inventory:
                if sound.type != "marker":
                    par_id = compute_id(str(sound))
                    values += [{
                        "ID": str(counter),
                        "Language_ID": language.id,
                        "Parameter_ID": par_id,
                        "Value": str(sound), 
                        }]
                    counter += 1
                    segments += [(
                        par_id, 
                        str(sound), 
                        sound.name
                        )]
        parameters = [{
                "ID": ID, 
                "Name": sound,
                "Description": desc,
                "CLTS_ID": desc.replace(' ', '_') if desc.strip() else "NA",
                "CLTS_BIPA": sound,
                "CLTS_Name": desc} for ID, sound, desc in set(segments)]


        cltstable = Terms()["cltsReference"].to_column().asdict()
        cltstable["datatype"]["format"] = "[a-z_-]+|NA"
        args.writer.cldf.add_columns(
                    'ParameterTable',
                    cltstable,
                    {'name': 'CLTS_BIPA', 'datatype': 'string'},
                    {'name': 'CLTS_Name', 'datatype': 'string'})
        args.writer.cldf.add_component(
            'LanguageTable',
            {'name': 'Forms', 'datatype': 'integer', 'dc:description': 'Number of forms'},
            {'name': "FormsWithSounds", "datatype": "integer",
                "dc:description": "Number of forms with sounds"},
            {'name': 'Concepts', 'datatype': 'integer', 'dc:description': 'Number of concepts'},
            {'name': 'Consonants', 'datatype': 'integer', 'dc:description': 'Number of consonants'},
            {'name': 'ConsonantsByQuality', 'datatype': 'integer',
                'dc:description': 'Number of consonants (ignoring length)'},
            {'name': 'ConsonantSounds', 'datatype': 'integer',
                'dc:description': 'Number of consonants (including complex clusters)'},
            {'name': 'Vowels', 'datatype': 'integer', 'dc:description': 'Number of vowels'},
            {'name': 'VowelsByQuality', 'datatype': 'integer',
                'dc:description': 'Number of vowels by quality'},
            {'name': 'VowelSounds', 'datatype': 'float', 'dc:description':
                'Vowels including diphthongs.'},
            {'name': 'WordLength', 'datatype': 'float', 'dc:description':
                'Average length per word'},
            {'name': 'SyllableLength', 'datatype': 'float', 'dc:description':
                'Average number of syllables per word.'},
            'Family'
            )
        args.writer.write(**{
                "ValueTable": values,
                "LanguageTable": languages,
                "ParameterTable": parameters,})


def run(args):
    dataset = get_dataset(args)
    with_dataset(args, 'makecldf', dataset=StructureDataset(dataset.dir))
    args.log.info('finished compiling the dataset')
