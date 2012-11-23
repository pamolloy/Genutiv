#
#   wiktionary.py
#
#   PURPOSE:
#   Find all article names under the specified categories on the German 
#   Wiktionary. Filter certain results and store the them in `dirty.json'.
#   All other nouns are stored in temporary `clean.json'.
#
#   TODO(PM) Output information
#   TODO(PM) Store removed data
#   TODO(PM) Error checking and handling
#   TODO(PM) Store category in Noun object
#   TODO(PM) extract_gender() is painfully slow
#

import re
import json
import codecs
import urllib2
import wikitools
from BeautifulSoup import BeautifulSoup
# Genutiv objects
from reference import Reference
from noun import Noun

class Wiktionary(Reference):
    """Download and crawl Wiktionary articles"""

    def __init__(self):
        Reference.__init__(self, 'German Wiktionary',
        'http://de.wiktionary.org/w/api.php', 'wiktionary.pickle')
        
        # Open dictionary of noun categories
        with open('reference/kategorien.json', 'r') as store:
            self.category_dict = json.load(store)

    def populate(self):
        """Create Noun objects from source and store them"""

        noun_set = self.lookup_nouns()

        for word in noun_set:
            noun = Noun(word)
            gender = self.lookup_gender(word)
            noun.setGender(gender)
            noun.setSourceName(self.title)
            noun.setSourceAddr(self.url)
            self.addNoun(noun)

    def lookup_nouns(self):
        """Populate a list with nouns"""

        base = set()

        #TODO(PM) Check/create `json' directory

        for category in self.category_dict['base']:
            base |= self.fetch(category)

        for category in self.category_dict['other']:
            base -= self.fetch(category)

        noun_set = self.filter(base)

        return noun_set

    def fetch(self, category_title):
        """Download set of words that are members of the input Wiktionary
        categories, unless they have already been stored"""

        print 'Loading members of: {}'.format(category_title)
        try:
            with codecs.open('json/' + category_title + '.json', 'r', 'utf-8') as store:
                word_list = json.load(store)
            word_set = set(word_list)
        except IOError:
            category = wikitools.category.Category(self.site, title=category_title)
            word_list = category.getAllMembers(titleonly=True)
            with codecs.open(category_title + '.json', 'w', 'utf-8') as store:
                json.dump(word_list, store)
            word_set = set(word_list)

        return word_set

    def filter(self, noun_set):
        """Remove nouns with a semicolon, dash or digit..."""

        clean = set()

        regex = re.compile('[:|\-|0-9]|\s')

        print 'Removing words with a semicolon, dash or digit.'
        for noun in noun_set:
            if not regex.search(noun):
                clean.add(noun)
            else:
                print u'Removing: {}'.format(noun)

        return clean

    def lookup_gender(self, noun):
        """Lookup gender for a noun"""

        print u'Looking up gender for `{}\''.format(noun)
        url = self.create_url(noun)
        page = self.get_html(url)
        gender = self.extract_gender(page)

        return gender

    def create_url(self, noun):
        """Return URL of noun on German Wiktionary"""

        url = u'http://de.wiktionary.org/wiki/{}'.format(noun)

        return url

    def get_html(self, url):
        """Download the page and read it"""

        user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30\
         Chrome/12.0.742.112 Safari/534.30'
       
        request = urllib2.Request(url.encode('utf-8'),
            headers = { 'User-Agent' : user_agent })
        raw_html = urllib2.urlopen(request)
        clean_html = raw_html.read()
        
        return clean_html 

    def extract_gender(self, page):
        """Use a regular expression on each line of web page until gender is
        found."""
        
        startline = re.compile('\s\(grammatikal..*')
        #endline = re.compile('Genus:\s')

        soup = BeautifulSoup(page)
        tags = soup.findAll('em')

        for em in tags:
            if 'Genus:' in em['title']:
                attribute = em['title']
                #attribute = startline.sub('', attribute)
                attribute = attribute[7:]
                #gender = endline.sub('', attribute)
                attribute = attribute.split(' ', 1)
                gender = attribute[0]
                print u'Found gender: {}'.format(gender)
                break

        return gender 

