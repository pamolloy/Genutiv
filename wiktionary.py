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
#   - Store date and time with data
#   - Only load necessary data from web page
#   - Compare to other crawling programs
#   - Patterns on page have relatively consistent line number
#   - Backup data structure while crawling
#   - Store pertinent information (e.g. date, time, source)
#   - Filter out Kategorie:Fremdwort
#

import urllib2
import wikitools
import re
import json
from BeautifulSoup import BeautifulSoup

class WikiNounList:
    """Create a list of nouns and filter false items."""
    
    def __init__(sef, username, password):
        self.clean = []
        self.dirty = []
        self.user = username
        self.word = password
    
    def titles(self, user, word):
        """Download list of Wiktionary category members."""
        
        # TODO(PM) Add an interface to login to de.wiktionary.org
        url = 'http://de.wiktionary.org/w/api.php'
        kategories = {
            'Deutsch':[], 
            'Substantiv':[], 
            'Eigenname (Deutsch)':[], # Subcategory of "Substantiv (Deutsch)"
            'Nachname (Deutsch)':[], # Subcategory of "Substantiv (Deutsch)"
            'Substantiv (Deutsch)':[], 
            'Substantiv (Althochdeutsch)':[], 
            'Substantiv (Mittelhochdeutsch)':[], 
            'Substantiv (Plattdetusch)':[], 
            'Fremdwort':[]
        }
        site = wikitools.wiki.Wiki(url, username=user, password=word)
        for kategorie in kategories:
            category = wikitools.category.Category(site, title=kategorie)
            kategories[kategorie] = category.getAllMembers(titleonly=True)
        return kategories
    
    def links():
        """Get information for filtering from links on each page."""
        
        pass
    
    def filter(self, kategories):
        """Remove list items that are not nouns."""
        
        # Remove colons, dashes, digits and spaces from category output
        regex = re.compile('[:|-|0-9]|\s')
        clean = [noun for noun in noun_list if not regex.search(noun) else dirty.append[noun] ]
    
    def save(self):
        """Save filtered nouns to JSON file and valid nouns to temporary 
        file."""
        
        with open('clean.json', 'w') as store:
            json.dump(clean, store)
        
        with open('dirty.json', 'w') as store:
            json.dump(dirty, store)

class WikiGender:
    user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30\
     Chrome/12.0.742.112 Safari/534.30'
    
    startline = re.compile('\s\(grammatikal..*')
    endline = re.compile('Genus:\s')
    url_space = re.compile(' ')
    
    noun_gender = {}
    
    def url_list():
        """Create a dictionary of nouns from cats.py and corresponding urls."""
        with open('nouns.json') as raw_nouns:
            noun_list = json.load(raw_nouns)

        urlz = {}

        for noun in noun_list:
            url_noun = url_space.sub('_', noun)
            url = 'http://de.wiktionary.org/wiki/{}'.format(url_noun)
            urlz[noun] = url
        return urlz

    def load_page(url):
        """For each URL in the given list: download the page, read it and split 
        into lines."""
        print 'Checking: {}'.format(url)
        request = urllib2.Request(url, headers = { 'User-Agent' : user_agent })
        raw_html = urllib2.urlopen(request)
        clean_html = raw_html.read()
        return clean_html

    def search_gender(page, noun):
        """Use a regular expression on each line of web page until gender is found."""
        soup = BeautifulSoup(page)
        for em in soup.findAll('em'):
            if 'Genus:' not in em['title']:
                continue
            attr_gender = em['title']
            attr_gender = startline.sub('', attr_gender)
            gender = endline.sub('', attr_gender)
            noun_gender[noun] = gender #Will this reference the global variable?
            print u'Found gender: {}'.format(gender)
            break

urlz = url_list()
for noun in urlz:
    url = urlz[noun]
    clean_html = load_page(url)
    search_gender(clean_html, noun)

with open('gender.json', 'wb') as store:
    json.dump(noun_gender, store)
