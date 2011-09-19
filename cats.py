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

## Should I login? Add interface to login?
site = wikitools.wiki.Wiki('http://de.wiktionary.org/w/api.php')
category = wikitools.category.Category(site, title='Substantiv (Deutsch)')

noun_list = category.getAllMembers(titleonly = True)

print "Processing list..."

regex = re.compile('[:|-|0-9]')
clean_list = [noun for noun in noun_list if not regex.search(noun)]

## Store data in file using pickle
## store object to be processed by nget.py 
with open('nouns.json', 'wb') as store:
    json.dump(clean_list, store)
