from csvw.dsv import UnicodeDictReader
from linse.profile import DraftProfile
from collections import defaultdict
from clldutils.text import strip_brackets
from unicodedata import normalize

with UnicodeDictReader('../cldf/forms.csv') as reader:
    data = [row for row in reader]

with UnicodeDictReader('../etc/orthography.tsv', delimiter="\t") as reader:
    profile = {}
    for row in reader:
        profile[normalize('NFC', row['Grapheme'])] = row['IPA']

languages = set([row['Language_ID'] for row in data])

profiles = {language: defaultdict(int) for language in languages}

errors = {}


lexemes = {}
for row in data:
    for char in row['Graphemes'].split():
        char = normalize('NFC', char)
        profiles[row['Language_ID']][char, profile.get(char, '?'+char)] += 1

    if [x for x in '˩˨˧˦˥' if x in row['Value']]:
        tone = False
        out = []
        for char in strip_brackets(row['Form']).split(' '):
            char = normalize('NFC', char)
            if [x for x in '˩˨˧˦˥' if x in char]:
                if tone:
                    out[-1] += char
                else:
                    out += [char]
                tone = True
            else:
                tone = False
                try:
                    out[-1] = char+out[-1]
                except IndexError:
                    out += [char]
        lexemes[row['Value']] = ''.join(out)

for language in languages:
    with open('../etc/orthography/'+language+'.tsv', 'w') as f:
        f.write('Grapheme\tIPA\tFrequency\n')
        for (char, ipa), freq in profiles[language].items():
            f.write('{0}\t{1}\t{2}\n'.format(char, ipa, freq))
            if ipa.startswith('?'):
                errors[char] = ipa[1:]

with open('../etc/lexemes2.tsv', 'w') as f:
    for a, b in lexemes.items():
        f.write(a+'\t'+b+'\tswap tones\n')

with open('addons.tsv', 'w') as f:
    for a, b in errors.items():
        f.write(a+'\t'+b+'\n')
