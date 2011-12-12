#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
#   wiktionary.py
#
#   PURPOSE:
#   Find all article names under the German noun category on the German 
#   Wiktionary. Filter certain results and store the them in dirty.json file.
#   All other nouns are stored in temporary clean.json file. Find gender for
#   each noun in clean.json and save in wiktionary.json file.
#
#   EXAMPLE:
#   e.g. list=categorymembers from http://en.wikipedia.org/w/api.php
#
#   TODO:
#   - Only load necessary data from web page
#   - Backup data structure while loading
#   - Store pertinent information (e.g. date, time, source)
#   - Filter out Kategorie:Fremdwort
#   - Use MediaWiki API prop module to find relevant templates (i.e. {{m}},
#      {{f}}, {{n}})
#   - Get information for filtering from links on each page.
#

import urllib2
import wikitools
import re
import json
from BeautifulSoup import BeautifulSoup


class WikiNounList(object):
    """Create a list of nouns and filter false items."""

    def __init__(self, url='http://de.wiktionary.org/w/api.php'):
        self.site = wikitools.wiki.Wiki(url) # TODO(PM) Add an interface to login to de.wiktionary.org
        self.nouns = {}
        with open('kategorien.json', 'r') as store:
            self.kategorien = json.dump(store)

    def fetch(self):
        """Download list of Wiktionary category members."""

        for kategorie in self.kategorien:
            category = wikitools.category.Category(self.site, title=kategorie)
            print 'Finding members of: {}'.format(kategorie)
            members = category.getAllMembers(titleonly=True) #TODO(PM) Create instance that returns a dictionary
            self.kategorien[kategorie] = members

        with open('full.json', 'wb') as store:
            json.dump(self.kategorien, store)

    def compare(self):
        """Remove elements of other categories from Substantiv (deutsch)"""

        with open('full.json', 'r') as store:
            kategorien = json.load(store)

        primary = kategorien['Substantiv (Deutsch)']
        primary = set(primary)
        del kategorien['Substantiv (Deutsch)']

        # TODO(PM) The toponym 'Kabul' was not filtered
        for category in kategorien:
            junk = set(kategorien[category])
            primary = primary - junk

        primary = list(primary) # JSON can not serialize 'set' objects
        
        primary = self.filter(primary)
        primary = self.gender(primary)
        
        with open('primary.json', 'wb') as store:
            json.dump(primary, store)

    def filter(self, nouns):
        """Remove list items that are not nouns."""

        clean = {}
        dirty = []
        regex = re.compile('[:|-|0-9]|\s')

        # Remove colons, dashes, digits and spaces from category output
        for noun in nouns:
            if not regex.search(noun):
                clean[noun] = ''
            else:
                dirty.append(noun)
        #clean = [noun if not regex.search(noun) else dirty.append[noun] for noun in nouns]

        return clean

    def gender(self, nouns):
        """Use MediaWiki API prop module to find relevant gender templates and
         assign gender to corresponding value"""

        for noun in nouns:
            page = wikitools.page.Page(self.site, title=noun)
            templates = page.getTemplates()

            for template in templates: #TODO(PM) Account for {{mf}}
                if template == u'Vorlage:f':
                    nouns[page.title] = "Femininum"
                    break
                elif template == u'Vorlage:m':
                    nouns[page.title] = "Maskulinum"
                    break
                elif template == u'Vorlage:n':
                    nouns[page.title] = "Neutrum"
                    break

        return nouns

edwin = WikiNounList()
edwin.compare()

#with open('gender-new.json', 'w') as store:
#    json.dump(noun_gender, store)
