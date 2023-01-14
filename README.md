# CLDF dataset derived from Greenhill et al.'s "Austronesian Basic Vocabulary Database" from 2020 focusing on Oceanic languages

[![CLDF validation](https://github.com/SimonGreenhill/abvd_oceanic/workflows/CLDF-validation/badge.svg)](https://github.com/SimonGreenhill/abvd_oceanic/actions?query=workflow%3ACLDF-validation)

## How to cite

If you use these data please cite
- the original source
  > Greenhill, S.J., Blust. R, & Gray, R.D. (2008). The Austronesian Basic Vocabulary Database: From Bioinformatics to Lexomics. Evolutionary Bioinformatics, 4:271-283.
- the derived dataset using the DOI of the [particular released version](../../releases/) you were using

## Description


This dataset is licensed under a CC-BY-4.0 license

Available online at https://abvd.shh.mpg.de/austronesian/


Conceptlists in Concepticon:
- [Blust-2008-210](https://concepticon.clld.org/contributions/Blust-2008-210)
## Notes

# Notes:

## Making a Nexus File:

You will need to have the lexibank dataset installed. Probably best outside the directory:




```shell
# set up and install a virtual environment
python -m venv env
source ./env/bin/activate

# clone git repository
git clone https://github.com/lexibank/abvdoceanic

# or update repository
cd abvd_oceanic
git checkout main
git pull
cd ..

# install dataset
cd abvd_oceanic
pip install -e .
cd ..
```

To make a nexus file, use the custom `abvdoceanic.nexus` in cldfbench. The parameters are:

* --output=/path/to/filename.nex = the output file to write.
* --ascertainment={token} add BEASTs ascertainment correction if you want.
* * `overall` - one ascertainment character added for overall correction.
* * `word` - per word ascertainment correction.
* --removecombined={int} - set level at which to filter combined cognates.


```shell
# make a nexus file, with combined cognates removed above level 2:
cldfbench abvdoceanic.nexus --removecombined 2 --output abvdoceanic.nex

# ...with per-word ascertainment correction:
cldfbench abvdoceanic.nexus --ascertainment=word --removecombined 2 --output abvdoceanic.nex
````






## Statistics


[![CLDF validation](https://github.com/SimonGreenhill/abvd_oceanic/workflows/CLDF-validation/badge.svg)](https://github.com/SimonGreenhill/abvd_oceanic/actions?query=workflow%3ACLDF-validation)
![Glottolog: 100%](https://img.shields.io/badge/Glottolog-100%25-brightgreen.svg "Glottolog: 100%")
![Concepticon: 100%](https://img.shields.io/badge/Concepticon-100%25-brightgreen.svg "Concepticon: 100%")
![Source: 0%](https://img.shields.io/badge/Source-0%25-red.svg "Source: 0%")
![BIPA: 100%](https://img.shields.io/badge/BIPA-100%25-brightgreen.svg "BIPA: 100%")
![CLTS SoundClass: 100%](https://img.shields.io/badge/CLTS%20SoundClass-100%25-brightgreen.svg "CLTS SoundClass: 100%")

- **Varieties:** 418
- **Concepts:** 191
- **Lexemes:** 78,515
- **Sources:** 0
- **Synonymy:** 1.14
- **Cognacy:** 74,236 cognates in 9,490 cognate sets (2,308 singletons)
- **Cognate Diversity:** 0.12
- **Invalid lexemes:** 0
- **Tokens:** 392,172
- **Segments:** 430 (0 BIPA errors, 0 CLTS sound class errors, 429 CLTS modified)
- **Inventory size (avg):** 30.58

## Possible Improvements:



- Entries missing sources: 78515/78515 (100.00%)

# Contributors

Name               | GitHub user     | Description                          | Role
---                | ---             | ---                                  | ---
Simon J. Greenhill | @SimonGreenhill | maintainer                           | Author
Johann-Mattis List | @lingulist  | orthography profiles | Other




## CLDF Datasets

The following CLDF datasets are available in [cldf](cldf):

- CLDF [Wordlist](https://github.com/cldf/cldf/tree/master/modules/Wordlist) at [cldf/cldf-metadata.json](cldf/cldf-metadata.json)