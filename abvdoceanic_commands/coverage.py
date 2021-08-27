"""
Calculate coverage statistics, cf. https://github.com/lexibank/abvdoceanic/issues/3
"""
from pathlib import Path

from cltoolkit import Wordlist
from pycldf import Dataset
from pyclts import CLTS
from tabulate import tabulate

from cldfbench.cli_util import with_dataset, get_dataset

def run(args):
    path = (Path(__file__).parents[1]).joinpath("cldf/cldf-metadata.json")
    # Load data
    bipa = CLTS().bipa
    wl = Wordlist([ Dataset.from_metadata(path) ], ts=bipa)
    
    # Create coverage table
    args.log.info("Creating coverage table...")
    table = []
    
    for language in wl.languages:
        table += [[language.name, len(language.concepts), len(language.forms_with_sounds),
                   len(language.sound_inventory.consonants), len(language.sound_inventory.vowels)]]
        
    return tabulate(table, headers=["Name", "Concepts", "Forms", "Consonants", "Vowels"], tablefmt="pipe")

