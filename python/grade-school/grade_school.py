#!/usr/bin/env python

"""
grade_school.py

Python script for the Python "Grade School", 'exercism' exercise.

A small archiving program that stores students' names along with the grade that they are in.

Created by: shamdela
Date:       25/10/2016
"""
from collections import defaultdict


class School:
    def __init__(self, name):
        self.name = name
        # defaultdict creates any items provided they do not exist yet.
        # Default dict items are created using set() in this instance, which returns a new empty set object.
        self.grade_dict = defaultdict(set)

    def add(self, student, grade):
        # The set.add() operation attaches the value to the new set.
        # When keys are encountered again, the look-up proceeds normally(returning the set for that key)
        # and the set.append() operation adds another value to the set.
        self.grade_dict[grade].add(student)

    def grade(self, grade):
        return self.grade_dict[grade]

    def sort(self):
        # Loops through all key, values in dictionary of grades, creates a new dictionary with grade again as key and a
        # sorted tuple of students as values. The dictionary is then sorted on key (grade).
        return sorted(((grade, tuple(sorted(student))) for grade, student in self.grade_dict.items()))

