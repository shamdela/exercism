#!/usr/bin/env python

"""
anagram.py

Python script for the Python "Anagram", 'exercism' exercise.

A program that, given a word and a list of possible anagrams, selects the correct sublist.
Given `"listen"` and a list of candidates like `"enlists" "google" "inlets" "banana"`
the program should return a list containing `"inlets"`.

Created by: shamdela
Date:       28/09/2016
"""
from collections import Counter


def detect_anagrams(word, anagram_list):
    anagrams = list()

    # Loop through list and use Counter package to compare word and each word in anagaram list.
    # The same word as itself isn't an anagram
    for possible_anagram in anagram_list:
        if (word.lower() != possible_anagram.lower()) and (Counter(word.lower()) == Counter(possible_anagram.lower())):
            anagrams.append(possible_anagram)

    return anagrams

