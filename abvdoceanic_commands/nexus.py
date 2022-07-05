"""
Write nexus file
"""
from pathlib import Path
from lexibank_abvdoceanic import Dataset as Oceanic
from nexusmaker import load_cldf
from nexusmaker import NexusMaker
from nexusmaker import NexusMakerAscertained
from nexusmaker import NexusMakerAscertainedParameters
from nexusmaker.tools import remove_combining_cognates

root = Path(__file__).parent.parent

def register(parser):
    parser.add_argument(
        "--output",
        default="abvdoceanic.nex",
        help="output file name")
    parser.add_argument(
        "--ascertainment",
        default=None,
        choices=[None, 'overall', 'word'],
        help="set ascertainment mode")
    parser.add_argument(
        "--filter",
        default=None,
        type=Path,
        help="filename containing a list of parameters (one per line) to remove")
    parser.add_argument(
        "--removecombined",
        default=None,
        type=int,
        help="set level at which to filter combined cognates")


def run(args):

    mdfile = root / 'cldf' / "cldf-metadata.json"
    args.log.info('loading %s' % mdfile)
    records = list(load_cldf(mdfile, table='FormTable'))
    
    # run filter if given
    if args.filter:
        for p in args.filter.read_text().split("\n"):
            p = p.lower()
            nrecords = len(records)
            records = [r for r in records if r.Parameter.lower() != p]
            change = nrecords - len(records)
            args.log.info(
                '%8d records removed for parameter %s' % (change, p)
            )
            if change == 0:
                args.log.warn(
                    "No records removed for parameter %s -- typo?" % p
                )

    args.log.info(
        'writing nexus from %d records to %s using ascertainment=%s'
        % (len(records), args.output, args.ascertainment)
    )

    if args.ascertainment is None:
        nex = NexusMaker(data=records)
    elif args.ascertainment == 'overall':
        nex = NexusMakerAscertained(data=records)
    elif args.ascertainment == 'word':
        nex = NexusMakerAscertainedParameters(data=records)
    else:
        raise ValueError("Unknown Ascertainment %s" % args.ascertainment)

    if args.removecombined:
        nex = remove_combining_cognates(nex, keep=args.removecombined)
        args.log.info(
            'removing combined cognates with more than %d components' % args.removecombined
        )

    nex.write(filename=args.output)
