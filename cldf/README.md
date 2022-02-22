<a name="ds-cldfmetadatajson"> </a>

# Wordlist CLDF dataset derived from Greenhill et al.'s "Austronesian Basic Vocabulary Database" from 2020 focusing on Oceanic languages

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

**Sources**: [sources.bib](./sources.bib)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Greenhill, S.J., Blust. R, & Gray, R.D. (2008). The Austronesian Basic Vocabulary Database: From Bioinformatics to Lexomics. Evolutionary Bioinformatics, 4:271-283.
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Wordlist](http://cldf.clld.org/v1.0/terms.rdf#Wordlist)
[dc:format](http://purl.org/dc/terms/format) | <ol><li>http://concepticon.clld.org/contributions/Blust-2008-210</li></ol>
[dc:identifier](http://purl.org/dc/terms/identifier) | https://abvd.shh.mpg.de/austronesian/
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | https://github.com/SimonGreenhill/abvd_oceanic
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="https://github.com/SimonGreenhill/abvd_oceanic/tree/82dfd28">SimonGreenhill/abvd_oceanic v0.1-103-g82dfd28</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.5">Glottolog v4.5</a></li><li><a href="https://github.com/concepticon/concepticon-data/tree/176a1946">Concepticon v2.5.0-47-g176a1946</a></li><li><a href="https://github.com/cldf-clts/clts/tree/v2.2.0">CLTS v2.2.0</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>lingpy-rcParams</strong>: <a href="./lingpy-rcParams.json">lingpy-rcParams.json</a></li><li><strong>python</strong>: 3.9.6</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | abvdoceanic
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-formscsv"></a>Table [forms.csv](./forms.csv)


Raw lexical data item as it can be pulled out of the original datasets.

This is the basis for creating rows in CLDF representations of the data by
- splitting the lexical item into forms
- cleaning the forms
- potentially tokenizing the form


property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF FormTable](http://cldf.clld.org/v1.0/terms.rdf#FormTable)
[dc:extent](http://purl.org/dc/terms/extent) | 78455


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Local_ID](http://purl.org/dc/terms/identifier) | `string` | 
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Parameter_ID](http://cldf.clld.org/v1.0/terms.rdf#parameterReference) | `string` | References [parameters.csv::ID](#table-parameterscsv)
[Value](http://cldf.clld.org/v1.0/terms.rdf#value) | `string` | 
[Form](http://cldf.clld.org/v1.0/terms.rdf#form) | `string` | 
[Segments](http://cldf.clld.org/v1.0/terms.rdf#segments) | list of `string` (separated by ` `) | 
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
`Cognacy` | `string` | 
`Loan` | `boolean` | 
`Graphemes` | `string` | 
`Profile` | `string` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 418


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
`Glottolog_Name` | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
`Family` | `string` | 
`author` | `string` | 
`url` | `string` | 
`typedby` | `string` | 
`checkedby` | `string` | 
`notes` | `string` | 
`source` | `string` | 

## <a name="table-parameterscsv"></a>Table [parameters.csv](./parameters.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ParameterTable](http://cldf.clld.org/v1.0/terms.rdf#ParameterTable)
[dc:extent](http://purl.org/dc/terms/extent) | 191


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Concepticon_ID](http://cldf.clld.org/v1.0/terms.rdf#concepticonReference) | `string` | 
`Concepticon_Gloss` | `string` | 

## <a name="table-cognatescsv"></a>Table [cognates.csv](./cognates.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF CognateTable](http://cldf.clld.org/v1.0/terms.rdf#CognateTable)
[dc:extent](http://purl.org/dc/terms/extent) | 74079


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Form_ID](http://cldf.clld.org/v1.0/terms.rdf#formReference) | `string` | References [forms.csv::ID](#table-formscsv)
[Form](http://linguistics-ontology.org/gold/2010/FormUnit) | `string` | 
[Cognateset_ID](http://cldf.clld.org/v1.0/terms.rdf#cognatesetReference) | `string` | 
`Doubt` | `boolean` | 
`Cognate_Detection_Method` | `string` | 
[Source](http://cldf.clld.org/v1.0/terms.rdf#source) | list of `string` (separated by `;`) | References [sources.bib::BibTeX-key](./sources.bib)
[Alignment](http://cldf.clld.org/v1.0/terms.rdf#alignment) | list of `string` (separated by ` `) | 
`Alignment_Method` | `string` | 
`Alignment_Source` | `string` | 

