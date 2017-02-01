#!/usr/bin/env python

"""
sum_of_multiples.py

Python script for the Python "Sum Of Multiples", 'exercism' exercise.

A program that, given a number, can find the sum of all the multiples of particular
numbers up to but not including that number.

Assumptions on Input to sum_of_multiples functions:
    - All input numbers are non-negative 'int's, i.e. natural numbers including
      zero.
    - A list of factors must be given, and its elements are unique and sorted in
      ascending order.

Created by: shamdela
Date:       17/10/2016
"""


def sum_of_multiples(number, factors):
    '''
    :param number: int
    :param factors: list
    :return: the sum of the multiples of the number
    '''
    multiples_list = set()

    if 0 in factors:
        factors.remove(0)

    for factor in factors:
        multiples_list.update(list(range(0, number, factor)))

    return sum(multiples_list)
