#!/usr/bin/env python

"""
allergies.py

Python script for the Python "Allergies", 'exercism' exercise.

A program that, given a person's allergy score, can tell them whether or not they're allergic to a given item,
and their full list of allergies.

Created by: shamdela
Date:       05/10/2016
"""


class Allergies:

    ALLERGY_SCORES = {
        'eggs': 1,
        'peanuts': 2,
        'shellfish': 4,
        'strawberries': 8,
        'tomatoes': 16,
        'chocolate': 32,
        'pollen': 64,
        'cats': 128
    }

    def __init__(self, score):
        self.score = score
        self.lst = list(allergy for allergy in self.ALLERGY_SCORES if
                        self.is_allergic_to(allergy))

    def is_allergic_to(self, allergen):
        return self.ALLERGY_SCORES[allergen] & self.score

