#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#   verity.py
#
#   PURPOSE: 
#   Print all correct and wrong nouns to individual files for processing by
#    kramdown.
#
#   TODO:
#

import codecs
import json

with open('compare.json') as store:
    results_dict = json.load(store)


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
        
        post.write(u'---\nlayout: post\ntitle: {0}\npermalink: genutiv/{0}\n---\n'.format(pattern_file))
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

print_file()

#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#   table.py
#
#   PURPOSE: 
#   Convert data structures into PHP Markdown Extra syntax for simple tables.
#
#   TODO:
#

import json
import codecs

file = codecs.open('table.txt', encoding='utf-8', mode='w+')

with open('accuracy.json') as raw:
    accuracy_dict = json.load(raw)

with open('example.json') as raw:
    example_dict = json.load(raw)

for gender in example_dict.keys():
    head = '== {} == \n'.format(gender)
    file.write(head)
    for pattern in example_dict[gender]:
        results = accuracy_dict[pattern]
        percent = results[0]
        
        example = example_dict[gender][pattern][0]
        root = example.split(' ')
        root = root[1]
        example = u'[{}](http://www.dict.cc/?s={})'.format(example, root)
        
        exception = example_dict[gender][pattern][1]
        if exception == '&hellip;':
            pass
        else:
            noun = exception.split(' ')
            noun = noun[1]
            exception = u'[{}](http://www.dict.cc/?s={})'.format(exception, noun)
        
        if pattern[-1] == '$':
            pattern_link = pattern[:-1]
            pattern = '-' + pattern[:-1]
        elif pattern[0] == '^':
            pattern_link = pattern[1:]
            pattern = pattern[1:] + '-'
        else: pass
       
        correct = results[1]
        correct = u'[{}](/genutiv/{}/#examples)'.format(correct, pattern_link)
        wrong = results[2]
        wrong = u'[{}](/genutiv/{}#exceptions)'.format(wrong, pattern_link)
        
        
        pattern = '`' + pattern + '`'
        line = u'{:9} | {:5}% | {:35} | {:55} | {:35} | {} \n'.format(pattern,percent,correct,example,wrong,exception)
        file.write(line)

file.close()
