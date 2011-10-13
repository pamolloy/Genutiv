#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
#   cats.py
#
#   PURPOSE:
#   Find all article names under the German noun category on the German 
#   Wiktionary, then store list of nouns in external file.
#
#   EXAMPLE:
#   e.g. list=categorymembers from http://en.wikipedia.org/w/api.php
#
#   TODO:
#   - Store date and time with data

import wikitools
import re
import json

print "Downloading list..."

# TODO(PM) Add an interface to login to de.wiktionary.org
site = wikitools.wiki.Wiki('http://de.wiktionary.org/w/api.php')
category = wikitools.category.Category(site, title='Substantiv (Deutsch)')

noun_list = category.getAllMembers(titleonly = True)

dirty_list = []

print "Processing list..."

# Remove colons, dashes and digits from category output
regex = re.compile('[:|-|0-9]')
clean_list = [noun for noun in noun_list if not regex.search(noun) else dirty_list.append[noun] ]

# Store object in JSON file to be processed by nget.py
with open('nouns.json', 'w') as store:
    json.dump(clean_list, store)

with open('nouns-dirty.json', 'w') as store:
    json.dump(dirty_list, store)
