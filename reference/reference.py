#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
#   reference.py
#
#   TODO
#   - Duck typing instead of testing for the type of arguments

from datetime import datetime
import wikitools

class Reference(object):
    """A reference for the source of the noun and its assigned gender"""

    def __init__(self, title, url):
        self.title = title
        self.url = url
        self.created = datetime.now()
        self.container = set()
        self.site = wikitools.wiki.Wiki(self.url)

    def addNoun(self, noun):
        """Add a Noun to the container"""

        self.container.add(noun)

    def removeNoun(self, noun):
        """Remove a Noun from the container"""
        #See: http://stackoverflow.com/questions/1267260

        self.container.remove(noun)

