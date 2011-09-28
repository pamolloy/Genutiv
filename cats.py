#!/usr/bin/python2.7
#
#   cats.py
#
#   Find all article names under the German noun category 
#   on the German Wiktionary. Print output list to file.
#

import wikitools
import re
import json

print "Downloading list..."

# TODO(PM) Add an interface to login to de.wiktionary.org
site = wikitools.wiki.Wiki('http://de.wiktionary.org/w/api.php')
category = wikitools.category.Category(site, title='Substantiv (Deutsch)')

noun_list = category.getAllMembers(titleonly = True)

print "Processing list..."

# Remove colons, dashes and digits from category output
regex = re.compile('[:|-|0-9]')
clean_list = [noun for noun in noun_list if not regex.search(noun)]

# Store object in JSON file to be processed by nget.py
with open('nouns.json', 'w') as store:
    json.dump(clean_list, store)
