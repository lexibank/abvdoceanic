#!/usr/bin/env python3
# coding=utf-8
"""..."""
__author__ = 'Simon J. Greenhill <simon@simon.net.nz>'
__copyright__ = 'Copyright (c) 2021 Simon J. Greenhill'
__license__ = 'New-style BSD'

import csvw
from pathlib import Path

def get(filename, delimiter=","):
    with csvw.UnicodeDictReader(filename, delimiter=delimiter) as reader:
        for row in reader:
            yield(row)

RAWDIR = Path('../raw')

keep = set()
for row in get('oceanicfiltered.txt', "\t"):
    keep.add(RAWDIR / ("%s.xml" % row['ID']))

for r in RAWDIR.iterdir():
    if r not in keep:
        print("rm %s" % r)
        r.unlink()
