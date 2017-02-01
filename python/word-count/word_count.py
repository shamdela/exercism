#!/usr/bin/env python

"""
word_count.py

Python script for the Python "Word Count", 'exercism' exercise.
Implementation of a program that given a phrase, can count the occurrences of each word in that phrase.

Created by: shamdela
Date:       19/09/2016
"""
import re


def word_count(phrase):
    word_counter = {}

    # RE to replace all non word chars with a space
    phrase = re.sub(r'\W|_+', "  ", phrase)

    # lowercase the phase and split on the default - space
    for word in phrase.lower().split():
        if word:
            word_counter[word] = word_counter.setdefault(word, 0) + 1

    return word_counter

