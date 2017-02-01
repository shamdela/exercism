#!/usr/bin/env python

"""
series.py

Python script for the Python "Series", 'exercism' exercise.

A program that will take a string of digits and give you all the contiguous substrings of length `n` in that string.

Created by: shamdela
Date:       07/10/2016
"""


def slices(digits, series):
    if series == 0 or series > len(digits):
        raise ValueError()

    lst = list()
    for i in range(len(digits)):
        if i + series <= len(digits):
            lst.append(list(map(int, digits[i:series+i])))
    return lst

