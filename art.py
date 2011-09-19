#!/usr/bin/python3.2
#
#   art.py
# 
#   Purpose: Guess the gender of German nouns
#       - Starting with singular nouns
#       - Incorporate exceptions
#       - Letters of the alphabet?!
#       - In compound words, both gender and plural are governed by the last word in the compound
#       - Nouns with dual gender
#

import re

print('Type a single German noun and hit enter')
noun = input()

## Usually Masculine
### Nouns ending in the suffixes -ig, -ling, -or, -us
### Nouns ending in -en
## Usually Feminine
### Words designating professions and nationalities, using the suffix -in with masculine forms
### Nouns ending in the suffixes -anz, -ei, -enz, -ie, -ik, -ion, -heit, -keit, -schaft, -tät, -ung, -ur, with exceptions (e.g. die Papagei)
### Most nouns ending in -e (plural -n)
## Usually Neuter
### Nouns ending in the suffix -tum (e.g. Christentum, Judentum, Eigentum), with exceptions (e.g. der Reichtum, der Irrtum)
### Diminutive suffixes -chen, -lein (and their dialect variations -erl, -el, -le, -li)
### Nouns with the suffixes -ment, -(i)um
### Most collective nouns beginning with the prefix Ge-

gender_dict = {'Maskulinum': ['ig$', 'ling$', 'or$', 'us$', 'en$'],
'Femininum': ['in$', 'erin$', 'anz$', 'ei$', 'enz$', 'ie$', 'ik$', 'ion$', 'heit$', 'keit$', 'schaft$', 'tät$', 'ung$', 'ur$', 'e$'],
'Neutrum': ['tum$', 'chen$', 'lein$', 'erl$', 'el$', 'le$', 'li$', 'ment$', 'ium$', 'um$', '^Ge']}

print('Checking input against patterns...')
for gender in gender_dict.keys():
    for pattern in gender_dict[gender]:
        if re.search(pattern, noun):
            if pattern[0] == '^':
                term = 'prefix'
                pattern = pattern[1:]
            elif pattern[-1] == '$':
                term = 'suffix'
                pattern = pattern[:-1]
            print('{0} matches the {3} -{1}, which means it is probably {2}.'.format(noun, pattern, gender, term))

