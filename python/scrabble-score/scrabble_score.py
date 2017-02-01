#!/usr/bin/env python

"""
scrabble_score.py

Python script for the "Scrabble Score", 'exercism' exercise.
A program that given a word, computes the scrabble score for that word.

Created by: shamdela
Date:       28/11/2016
"""
import re

SCORE_DICT = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1, 'n': 1, 'r': 1, 's': 1, 't': 1,
              'd': 2, 'g': 2,
              'b': 3, 'c': 3, 'm': 3, 'p': 3,
              'f': 4, 'h': 4, 'v': 4, 'w': 4, 'y': 4,
              'k': 5,
              'j': 8, 'x': '8',
              'q': 10, 'z': 10}


def score(scrabble_word):
    """ Takes a word and returns is scrabble score based off scoring dictionary above
    :param scrabble_word:
    :return: scrabble score for each word
    """
    if re.search(r"[\d\s]", scrabble_word):
        return 0
    return sum(int(SCORE_DICT[letter.lower()]) for letter in scrabble_word)

