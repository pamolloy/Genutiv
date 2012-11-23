#!/usr/bin/python2
# -*- coding: utf-8 -*-
#
#   analysis.py
#
#   PURPOSE: 
#   Create a data structure with nouns matched to patterns and access whether
#   pattern could accurately guess gender of each matched noun.
#
#   TODO(PM) Test the percent accuracy of each default pattern.
#

import json

with open('compare.json') as store:
    results_dict = json.load(store)

with open('pattern.json') as store:
    pattern_dict = json.load(store)


def list_prompt():
    """List requested analyzed patterns."""
    
    print 'TYPE: Maskulinum, Femininum, Neutrum, or All'
    select = raw_input('> ')
    
    if select == 'All':
        for gender in pattern_dict.keys():
            list_patterns(gender)
    elif select == ('Maskulinum' or 'Feminunum' or 'Neutrum'):
        list_patterns(select)
    else: print 'Please check your input!'

def list_patterns(gender):
    """Print formatted patterns for gender."""
    
    for pattern in pattern_dict[gender]:
        if pattern[-1] == '$':
            print '-' + pattern[:-1]
        elif pattern[0] == '^':
            print pattern[1:] + '-'
        else: pass

def results():
    """Create a dictionary containing results of accuracy test."""
    
    accuracy_dict = {}
    exception_list = {}

    for pattern in results_dict.keys():
        solution = accuracy(pattern)
        accuracy_dict[pattern] = solution
        
        exceptions = exception(pattern)
        exception_list[pattern] = exceptions
    
    with open('stat.json', 'w') as store:
        json.dump(accuracy_dict, store)
    
    with open('exception.json', 'w') as store:
        json.dump(exception_list, store)

def accuracy(pattern):
    """Test the percent accuracy of a default pattern."""
    
    correct = 0
    wrong = 0
    
    for result in results_dict[pattern].values():
        if result == 'Correct':
            correct += 1
        elif result == 'Wrong':
            wrong += 1
        else: pass 
    
    percent = (float(correct) / (float(correct) + float(wrong))) * 100
    rpercent = round(percent, 1)
    solution = [rpercent, correct, wrong]

    return solution


# Nouns correctly matched by pattern
results()
#list_prompt()
