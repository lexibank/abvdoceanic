"""
Write nexus file
"""
from lexibank_abvdoutliers import Dataset as Outliers
from nexusmaker import load_cldf, NexusMaker, NexusMakerAscertained, NexusMakerAscertainedParameters


def register(parser):
    parser.add_argument("--output",
        default="abvdoceanic.nex",
        help="output file name")
    parser.add_argument("--ascertainment",
        default=None,
        choices=[None, 'overall', 'word'],
        help="set ascertainment mode")


def run(args):
    mdfile = Outliers().cldf_dir / "cldf-metadata.json"
    args.log.info('loading %s' % mdfile)
    records = list(load_cldf(mdfile, table='FormTable'))
    args.log.info('writing nexus from %d records to %s using ascertainment=%s' % (
        len(records), args.output, args.ascertainment
    ))
    
    if args.ascertainment is None:
        nex = NexusMaker(data=records)
    elif args.ascertainment == 'overall':
        nex = NexusMakerAscertained(data=records)
    elif args.ascertainment == 'word':
        nex = NexusMakerAscertainedParameters(data=records)
    else:
        raise ValueError("Unknown Ascertainment %s" % args.ascertainment)

    nex.write(filename=args.output)