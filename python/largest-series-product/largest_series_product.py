#!/usr/bin/env python

"""
largest_series_product.py

Python script for the Python "Largest Series Product", 'exercism' exercise.

A program that when given a string of digits, can calculate the largest product for a
contiguous substring of digits of length n.

Created by: shamdela
Date:       24/10/2016
"""
from functools import reduce
import operator


def largest_product(digits, digit_length):
    """
    Loops through each digit and creates a slice for each contiguous  pair, then maps this to an int before calling
    reduce function to multiply each digit and append result back to a list

    :param digits:
    :param digit_length:
    :return: max value in list
    """

    if digit_length > len(digits) or digit_length < 0:
        raise ValueError("Invalid digit length provided")

    if not digits or digit_length == 0:
        return 1

    product_list = list()
    for idx, val in enumerate(digits):
        if idx + digit_length <= len(digits):
            product_list.append(reduce(operator.mul, tuple(map(int, digits[idx: idx + digit_length]))))

    return max(product_list)
