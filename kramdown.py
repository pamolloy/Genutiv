#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#   kramdown.py
#
#   PURPOSE: 
#   Convert data structures into PHP Markdown Extra syntax for simple tables.
#   Print all correct and wrong nouns to individual pages for processing by
#   kramdown and to be linked to in table.
#
#   TODO:
#   - If a page exists on Wiktionary then link morpheme in table
#

import codecs
import json

with open('comparison.json') as store:
    results_dict = json.load(store)

with open('anaylsisjson') as raw:
    analysis_dict = json.load(raw)

with open('example.json') as raw:
    example_dict = json.load(raw)

with codecs.open('table.txt', encoding='utf-8', mode='w+') as table_file:

class Pages(object):
    """Create a page for each pattern containing exception and example 
    nouns."""

    def print_file():
        """Open pattern file and write noun examples and exceptions along with
        liquid and kramdown formatting."""
        
        for pattern in results_dict.keys():
            if pattern[-1] == '$':
                pattern_file = pattern[:-1]
            elif pattern[0] == '^':
                pattern_file = pattern[1:]
            else: pass
            
            file = 'verity/2011-10-14-' + pattern_file + '.md'
            post = codecs.open(file, encoding="utf-8", mode="w+")
            
            correct = list_nouns(pattern, 'Correct')
            wrong = list_nouns(pattern, 'Wrong')
            
            post.write(u'---\nlayout: post\ntitle: {0}\n
                permalink: genutiv/{0}\n---\n'.format(pattern_file))
            post.write('## Examples ## {#examples}\n')
            for noun in correct:
                post.write(noun + ' ')
            post.write('\n')
            post.write('\n## Exceptions ## {#exceptions}\n')
            for noun in wrong:
                post.write(noun + ' ')

    def list_nouns(pattern, verity):
        """Return all nouns that match pattern and correctly predict gender."""
        
        verity_list = []
        
        for noun in results_dict[pattern].keys():
            if results_dict[pattern][noun] == verity:
                verity_list.append(noun)
        
        return verity_list

class PrintTables(object):
    
    def __init__(self):
    
    def gender():
        """Create a section for each gender."""

        for gender in example_dict.keys():
            head = '== {} == \n'.format(gender)
            table_file.write(head)
            
    def row():
        """Create a list of all examples and exceptions."""
        
        for pattern in example_dict[gender]:
            results = analysis_dict[pattern]
            
            precent(results)
            correct(results)
            wrong(results)
            example(gender, pattern)
            exception(gender, pattern)
            
            line = u'{:9} | {:5}% | {:35} | {:55} | {:35} | {} \n'.format(
                pattern, percent, correct, example, wrong, exception
                )
            table_file.write(line)
            
    def pattern(self, pattern):
        """Format the pattern to be displayed in a table."""
        
        # Remove regular expression metacharacters
        if pattern[-1] == '$':
            pattern_link = pattern[:-1]
            pattern = '-' + pattern[:-1]
        elif pattern[0] == '^':
            pattern_link = pattern[1:]
            pattern = pattern[1:] + '-'
        else: pass
        
        pattern = '`' + pattern + '`' # Add <code> tag around pattern
        
        return pattern
        
    def percent(self, results):
        """Return the percent accuracy of a pattern."""
        
        percent = results[0]
        
        return percent
        
    def correct(self, results):
        """Return the total number of nouns correctly matched with a link to 
        the example section of the pattern page."""
        
        correct = results[1]
        correct = u'[{}](/genutiv/{}/#examples)'.format(correct, pattern_link)
        
        return correct
        
    def wrong(self, results):
        """Return the total number of nouns incorrectly matched with a link 
        to the exception section of the pattern page."""
        
        wrong = results[2]
        wrong = u'[{}](/genutiv/{}#exceptions)'.format(wrong, pattern_link)
        
        return wrong
        
    def example(self, gender, pattern):
        """Format an example from example.json file."""
        
        example = example_dict[gender][pattern][0]
        noun = example.split(' ')
        noun = noun[1]
        example = u'[{}](http://www.dict.cc/?s={})'.format(example, noun)
        
        return example
        
    def exception(self, gender, pattern):
        """Format an exception from example.json file."""
        
        exception = example_dict[gender][pattern][1]
        
        if exception == '&hellip;':
            pass
        else:
            noun = exception.split(' ')
            noun = noun[1]
            exception = u'[{}](http://www.dict.cc/?s={})'.format(
                exception, noun
                )
        
        return exception
        
