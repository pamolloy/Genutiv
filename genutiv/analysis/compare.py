#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#   art.py
#
#   PURPOSE: 
#   Create a data structure with nouns matched to patterns and assess whether
#   pattern could accurately guess gender of each matched noun.
#
#   TODO(PM) There are numerous data structures in this script. Is it better to
#     build them like pattern_dict or reverse_pattern_dict? And then under
#     what circumstances?
#   TODO(PM) Can I factor out the for loops into a more generic function?
#

import json
import re


with open('pattern.json') as pattern_file:
    pattern_dict = json.load(pattern_file)


# Load noun:gender dictionary
with open('gender.json') as gender_file:
    gender_dict = json.load(gender_file)

def patterns():
    """Transform pattern_dict to pattern:gender for simple comparison later."""
    
    reverse_pattern_dict = {}
    
    # Should I use nested dictionary comprehensions here?
    for gender in pattern_dict:
        for pattern in pattern_dict[gender]:
            reverse_pattern_dict[pattern] = gender
    
    return reverse_pattern_dict

def matches(reverse_dict):
    """Create a series of pattern dictionaries containing matching nouns."""
    
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
    return match_dict

def compare(reverse_dict, match_dict):
    """Match pattern guess gender with real noun gender."""
    
    for pattern in match_dict:
        for noun in match_dict[pattern].keys():
            noun_gender = reverse_dict[pattern]
            if gender_dict[noun] == noun_gender:
                match_dict[pattern][noun] = 'Correct'
            else:
                match_dict[pattern][noun] = 'Wrong' #Why is it wrong?
    return match_dict

reverse_dict = patterns()
match_dict = matches(reverse_dict)
comparison = compare(reverse_dict, match_dict)

with open('compare.json', 'wb') as store:
    json.dump(match_dict, store)
