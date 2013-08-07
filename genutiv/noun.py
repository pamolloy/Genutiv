# -*- coding: utf-8 -*-
#
#   noun.py
#

from datetime import datetime

class Noun(object):
    """A German noun"""

    def __init__(self, noun):
        self.noun = noun
        self.created = datetime.now()
        self.updated = self.created
        self.gender = ''
        self.sourceName = ''
        self.sourceAddr = ''

    def updateTime(self):
        self.updated = datetime.now()

    def setGender(self, gender):
        self.gender = gender
        self.updateTime

    def setSourceName(self, name):
        self.sourceName = name
        self.updateTime

    def setSourceAddr(self, address):
        self.sourceAddr = address
        self.updateTime

class WikiNoun(Noun):
    """A German noun generated by the German Wiktionary"""

    def __init__(self, noun, ref, cat):
        Noun.__init__(self, noun, ref)
        self.category = cat

