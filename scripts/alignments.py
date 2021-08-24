from lingpy import *

wl = Wordlist.from_cldf(
        "../cldf/cldf-metadata.json", 
        columns=[
            "language_id",
            "concept_name",
            "value",
            "form",
            "segments",
            "cognacy"])

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
alms = Alignments(wl, ref="cogid", transcription="form")
alms.align()
alms.output('tsv', filename="aligned-data", ignore="all", prettify=False)

