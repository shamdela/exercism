#!/usr/bin/env python

"""
bob.py

Python script for the Python "Bob", 'exercism' exercise.

Bob is a lackadaisical teenager. In conversation, his responses are very limited.
Bob answers 'Sure.' if you ask him a question.
He answers 'Whoa, chill out!' if you yell at him.
He says 'Fine. Be that way!' if you address him without actually saying anything.
He answers 'Whatever.' to anything else.

Created by: shamdela
Date:       20/09/2016
"""


def hey(what):
    if what.isupper():
        return 'Whoa, chill out!'
    elif what.strip().endswith('?'):
        return 'Sure.'
    elif what.strip() == '':
        return 'Fine. Be that way!'
    return 'Whatever.'

