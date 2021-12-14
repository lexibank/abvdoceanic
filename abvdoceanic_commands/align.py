"""
Align the data to be able to inspect the data in EDICTOR.
"""
from lingpy import *
from lexibank_abvdoceanic import Dataset


def register(parser):
    parser.add_argument(
            "--output",
            default="file",
            help="output file name"
            )

def run(args):
    wl = Wordlist.from_cldf(
            str(Dataset().cldf_dir / "cldf-metadata.json"), 
            columns=[
                "language_id",
                "concept_name",
                "value",
                "form",
                "segments",
                "cognacy"])
    args.log.info("loaded wordlist")
    
    # get the "true" cognate sets
    C, cognates = {}, {}
    cogid = 1
    for idx, concept, cognacy in wl.iter_rows("concept", "cognacy"):
        if not cognacy:
            C[idx] = cogid
            cogid += 1
        else:
            if cognacy.isdigit():
                cognateset = cognacy+'-'+concept
            else:
                cognateset = cognacy.split(',')[0]+'-'+concept
            if cognateset not in cognates:
                cognates[cognateset] = cogid
                cogid += 1
            C[idx] = cognates[cognateset]
    wl.add_entries('cogid', C, lambda x: x)
    args.log.info('added cognate sets')
    alms = Alignments(wl, ref="cogid", transcription="form")
    args.log.info('loaded the alignments')
    alms.align()
    alms.output('tsv', filename=args.output, ignore="all", prettify=False)
    args.log.info("output written to file "+args.output+".tsv")

