#!/usr/bin/env python

"""
pangram.py

Python script for the Python "Pangram", 'exercism' exercise.
Determine if a sentence is a pangram.
A pangram is a sentence using every letter of the alphabet at least once.
The best known English pangram is "The quick brown fox jumps over the lazy dog."

Created by: shamdela
Date:       16/09/2016
"""
import string


def is_pangram(sentence):
    if not sentence:
        return False

    # Create 2 sets.
    # 1st containing all lower case letters in alphabet
    # 2nd containing all lowercase letters that are in sentence but also in alphabet_set
    alphabet_set = set(string.ascii_lowercase)
    sentence_set = {letter for letter in sentence.lower() if letter in alphabet_set }

    if len(sentence_set) != len(alphabet_set):
        return False

    return True
