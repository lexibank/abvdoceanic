# Workflow Description

The starting point is to install CLDFBench and Pylexibank, etc.:

The easiest way to do so is with PIP:

```
$ pip install -e .
```

Then, you can create the lexical CLDF data (please make sure to configure your catalogs for concepticon, clts, and glottolog before):

```
$ cldfbench lexibank.makecldf lexibank_abvdoceanic.py --clts-version=v2.1.0 --glottolog-version=v4.4 --concepticon-version=v2.5.0 
```

To create the structural data, type:

```
$ cldfbench abvdoceanic.structure lexibank_abvdoceanic.py
```

This will create the data in the folder `cldf-structure/`.

To plot consonant and vowel inventories in an interactive map, install `cldfviz` and type:

```
$ cldfbench cldfviz.map --language-properties=Consonants,Vowels --format html --markersize 20 cldf-structure/StructureDataset-metadata.json --pacific-centered --output=plots/map
```

If you have `cartopy` installed, you can also plot the data in PDF format:

```
$ cldfbench cldfviz.map --language-properties=Consonants,Vowels --format pdf --width 30 --height 20 --markersize 20 cldf-structure/StructureDataset-metadata.json --extent=-40,80,30,-50 --pacific-centered --output=plots/map
```
