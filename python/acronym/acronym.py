#!/usr/bin/env python

"""
acronym.py

Python script for the Python "Acronym", 'exercism' exercise.

A program that converts a long phrase to its acronym


Created by: shamdela
Date:       19/10/2016
"""
import re

WORD_PATTERN = re.compile('[A-Z]?[a-z]+|[A-Z]+')


def abbreviate(phrase):
    """
    A function that will take in a phrase, run a regex pattern match and return the phrase's acronym

    :param phrase:
    :return: string of uppercase letters - the acronym
    """
    word_list = re.findall(WORD_PATTERN, phrase)
    return "".join(word[0] for word in word_list).upper()
