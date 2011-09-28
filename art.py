#!/usr/bin/python2
#
#   art.py
# 
#   TODO
#       - In compound words, both gender and plural are governed by the last
#          word in the compound
#       - Nouns with dual gender
#       - There are numerous data structures in this script. Is it better to
#          build them like pattern_dict or reverse_pattern_dict? And then under
#          what circumstances?
#       - How many nouns don't match a pattern, and what nouns are they?
#       - Can I factor out the for loops into a more generic function?

#   Masculine
#       - Nouns ending in the suffixes -ig, -ling, -or, -us
#       - Nouns ending in -en
#   Feminine
#       - Words designating professions and nationalities, using the suffix -in
#          with masculine forms
#       - Nouns ending in the suffixes -anz, -ei, -enz, -ie, -ik, -ion, -heit,
#          -keit, -schaft, -tät, -ung, -ur, with exceptions (e.g. die Papagei)
#       - Most nouns ending in -e (plural -n)
#   Neuter
#       - Nouns ending in the suffix -tum (e.g. Christentum, Judentum, 
#          Eigentum), with exceptions (e.g. der Reichtum, der Irrtum)
#       - Diminutive suffixes -chen, -lein (and their dialect variations -erl,
#          -el, -le, -li)
#       - Nouns with the suffixes -ment, -(i)um
#       - Most collective nouns beginning with the prefix Ge-

from __future__ import print_function
import json
import re

pattern_dict = {'Maskulinum': ['ig$', 'ling$', 'or$', 'us$', 'en$'],
 'Femininum': ['in$', 'erin$', 'anz$', 'ei$', 'enz$', 'ie$', 'ik$', 'ion$',
 'heit$', 'keit$', 'schaft$', 'ung$', 'ur$', 'e$'],
 'Neutrum': ['tum$', 'chen$', 'lein$', 'erl$', 'el$', 'le$', 'li$', 'ment$',
 'ium$', 'um$', '^Ge']}

# Load noun:gender dictionary
with open('gender.json') as gender_file:
    gender_dict = json.load(gender_file)

def patterns():
    '''Transform pattern_dict to pattern:gender for simple comparison later.'''
    
    reverse_pattern_dict = {}
    
    # Should I use nested dictionary comprehensions here?
    for gender in pattern_dict:
        for pattern in pattern_dict[gender]:
            reverse_pattern_dict[pattern] = gender
    
    return reverse_pattern_dict

def matches(reverse_dict):
    '''Create a series of pattern dictionaries containing matching nouns.'''
    
    match_dict = {}
    
    # Add patterns as keys to match_dict
    # Can be added to following for loop
    for pattern in reverse_dict.keys():
        match_dict[pattern] = {}
    
    # If noun in gender_dict matches a pattern add it to match_dict
    for noun in gender_dict.keys():
        for pattern in reverse_dict.keys():
            if re.search(pattern, noun):
                match_dict[pattern][noun] = ''
#                noun_utf = noun.encode('utf8') # Loaded as ascii
#                print('Matched {0} to {1}'.format(noun_utf, pattern))
#                print(match_dict)
    return match_dict

def compare(reverse_dict, match_dict):
    '''Match pattern guess gender with real noun gender.'''
    
    for pattern in match_dict:
        for noun in match_dict[pattern].keys():
            noun_gender = reverse_dict[pattern]
            if gender_dict[noun] == noun_gender:
                match_dict[pattern][noun] = 'Correct'
            else:
                match_dict[pattern][noun] = 'Wrong' #Why is it wrong?
    return match_dict

def results(compare_dict):
    '''Print requested data from comparison.'''
    
    # Accuracy of a pattern
    for pattern in compare_dict.keys():
        total = len(compare_dict[pattern])
        correct = 0
        wrong = 0
        other = 0
        
        for result in compare_dict[pattern].values():
            if result == 'Correct':
                correct += 1
            elif result == 'Wrong':
                wrong += 1
            else:
                other += 1
        
        accuracy = round((float(correct) / float(total)) * 100, 2)
        print('"{0}": {1}% for {2} nouns'.format(pattern, accuracy, total))

    # Any exceptions to a pattern
    # Nouns correctly matched by pattern

reverse_dict = patterns()
match_dict = matches(reverse_dict)
comparison = compare(reverse_dict, match_dict)
results(comparison)

#with open('compare.json', 'wb') as store:
#    json.dump(match_dict, store)
