#!/usr/bin/env python

"""
matrix.py

Python script for the "Matrix", 'exercism' exercise.
A program that, given a string representing a matrix of numbers, can return the rows and
columns of that matrix.

Created by: shamdela
Date:       13/01/2017
"""


class Matrix:
    """ A class object, matrix that only contains an initialise method to parse incoming string and define
    rows and columns """
    def __init__(self, str_matrix):
        # Split string on newline and loop on each pair
        # Then split each pair on spaces, convert from str to int and append list of ints to a rows list
        self.rows = [list(map(int, pair.split())) for pair in str_matrix.split('\n')]

        # Set columns by transposing the rows. zip takes in n lists and "zips" them:
        # zip([1,2,3], [4,5,6]) will become [(1,4), (2,5), (3,6)]
        # The * tells a function to use the elements of whatever follows as your arguments and not the object itself
        self.columns = [list(column) for column in zip(*self.rows)]
