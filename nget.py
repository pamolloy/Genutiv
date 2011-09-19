#!/usr/bin/python2
#
#   nget.py
#
#   Use available APIs to collect data
#   e.g. list=categorymembers from http://en.wikipedia.org/w/api.php
#
#   - Only load necessary data from web page
#   - Compare to other crawling programs
#   - Patterns on page have relatively consistent line number
#
## Match the following pattern on each page:
# ex. <em title="Genus: Femininum (grammatikal. Geschlecht: weiblich)">f</em>


from __future__ import print_function
import urllib2
import re
import json
import logging
from BeautifulSoup import BeautifulSoup

logging.basicConfig(level=logging.DEBUG)
LOG = logging.getLogger(__name__)

user_agent = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.30 Chrome/12.0.742.112 Safari/534.30'
startline = re.compile('\s\(grammatikal..*')
endline = re.compile('Genus:\s')
noun_gender = {}

def url_list():
    with open('nouns.json') as raw_nouns:
        noun_list = json.load(raw_nouns) #Create a list of nouns from output of cats.py

    urlz = {}

    for noun in noun_list:
        url = u'http://de.wiktionary.org/wiki/{}'.format(noun)
        urlz[noun] = url
    return urlz

def load_page(url):
    """For each URL in the given list: download the page, read it and split into lines."""
    print(u'Checking: {}'.format(url))
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
        print(u'Found gender: {}'.format(gender)) #How do I reference the noun variable here?
        break

urlz = url_list()
count = 0
for noun in urlz:
    count += 1
    url = urlz[noun]
    clean_html = load_page(url)
    search_gender(clean_html, noun)
    if count > 10:
        break

with open('gender.json', 'wb') as store:
    json.dump(noun_gender, store)
