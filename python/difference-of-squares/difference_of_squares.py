#!/usr/bin/env python

"""
difference_of_squares.py

Python script for the Python "Difference Of Squares", 'exercism' exercise.
Finds the difference between the sum of the squares and the square of the sums of the first N natural numbers.

Created by: shamdela
Date:       27/09/2016
"""


def difference(number):
    return square_of_sum(number) - sum_of_squares(number)


def square_of_sum(number):
    return sum([x for x in range(number + 1)]) ** 2


def sum_of_squares(number):
    return sum(x * x for x in range(number + 1))

