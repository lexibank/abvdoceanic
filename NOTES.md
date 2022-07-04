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



