#!/usr/bin/env python

"""
kindergarten_garden.py

Python script for the Python "Kindergarten Garden", 'exercism' exercise.

A program that given a diagram, can tell you which plants each child in the kindergarten class is responsible for.

Created by: shamdela
Date:       25/10/2016
"""
CHILDREN = ['Alice',
            'Bob',
            'Charlie',
            'David',
            'Eve',
            'Fred',
            'Ginny',
            'Harriet',
            'Ileana',
            'Joseph',
            'Kincaid',
            'Larry']

PLANT_DICT = {'C': 'Clover',
              'G': 'Grass',
              'R': 'Radishes',
              'V': 'Violets'}

PLANTS_PER_CHILD = 2


class Garden:

    def __init__(self, plant_rows, students=CHILDREN):
        self.plant_row1, self.plant_row2 = plant_rows.split('\n')
        self.students = sorted(students)

    def plants(self, child):
        idx_offset = self.students.index(child) * 2
        row1 = [PLANT_DICT[letter] for letter in self.plant_row1[idx_offset: idx_offset + PLANTS_PER_CHILD]]
        row2 = [PLANT_DICT[letter] for letter in self.plant_row2[idx_offset: idx_offset + PLANTS_PER_CHILD]]
        return row1 + row2
