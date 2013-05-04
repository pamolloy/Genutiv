# -*- coding: utf-8 -*-
#
#   genutiv.py
#
# Test the accuracy of patterns commonly cited in educational literature
# to help guess the gender of German nouns.
#

from reference.wiktionary import Wiktionary

if __name__ == '__main__':
    container = set()
    wiki = Wiktionary()
    wiki.populate()

