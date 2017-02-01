#!/usr/bin/env python

"""
flatten_array.py

Python script for the Python "Flatten Array", 'exercism' exercise.

A program that will take a nested list and returns a single list with all values except nil/null

Created by: shamdela
Date:       27/10/2016
"""
from collections import Iterable


def flatten(nested_list):
    """
    Main function
    :param nested_list:
    :return: An unflattened list
    """
    return [element for element in flatten_list(nested_list)]


def flatten_list(nested_list, ignore_types=(str)):
    """
    A recursive generator function involving a 'yield from' statement.
    :param nested_list:
    :param ignore_types:
    :return: Yields values in the list
    """
    for x in nested_list:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        elif x is not None:
                yield x

