#!/usr/bin/env python3
# coding=utf-8
"""
Updates language data in this snapshot to match the (more up-to-date)
ABVD lexibank dataset.
"""
import warnings
from pathlib import Path
from shutil import copyfile


ABVD_LEXIBANK = Path('../../abvd/raw/')

xmlfiles = {x.name: x for x in ABVD_LEXIBANK.glob("*.xml")}

for p in Path('.').glob("*.xml"):
    if p.name in xmlfiles:
        print("cp %s ." % xmlfiles[p.name])
        
#
#
# with csvw.UnicodeDictReader(WANTED_OCEANIC_LANGUAGES, delimiter="\t") as reader:
#     for row in reader:
#         wanted = Path("%s.xml" % row['ID'])
#         if str(wanted) in xmlfiles:
#             print(
#                 'overwrite' if wanted.exists() else 'copy',
#                 xmlfiles[str(wanted)], '->', wanted
#             )
#             copyfile(xmlfiles[str(wanted)], wanted)
#         else:
#             if not wanted.exists():
#                 warnings.warn(
#                     '%s should be deleted -- not in %s' % (
#                     wanted, ABVD_LEXIBANK_SNAPSHOT
#                 ))
