#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
#   reference.py
#
#   TODO
#   - Duck typing instead of testing for the type of arguments

from datetime import datetime
import wikitools
import pickle

class Reference(object):
    """A reference for the source of the noun and its assigned gender"""

    def __init__(self, title, url, filename):
        self.title = title
        self.url = url
        self.filename = filename
        self.container = set()
        self.site = wikitools.wiki.Wiki(self.url)

        # Open set of Noun objects
        try:
            with open(self.filename, 'rb') as store:
                self.container = pickle.load(store)
        except IOError as e:
            print 'File not found'

    def addNoun(self, noun):
        """Add a Noun to the container"""

        self.container.add(noun)
        with open(self.filename, 'wb') as store:
            pickle.dump(noun, store, pickle.HIGHEST_PROTOCOL)

    def removeNoun(self, noun):
        """Remove a Noun from the container"""
        #See: http://stackoverflow.com/questions/1267260

        self.container.remove(noun)

