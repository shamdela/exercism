#!/usr/bin/env python

"""
prime_factors.py

Python script for the Python "Prime Factors", 'exercism' exercise.
A program to compute the prime factors of a given natural number.

Created by: shamdela
Date:       14/11/2016
"""
from functools import reduce
import operator


def prime_factors(natural_number):
    """ A function that takes a natural number, uses recursion to calculate
    this number's prime factors numbers, and returns them in a list

    :param natural_number:
    :return: A list of prime factors of the natural number
    """

    prime_factor_list = []  # list to store prime factor numbers

    # Starting at 2, loop through all numbers up to the natural number, and use
    # divmod to check if the natural number is divisible by each number in loop
    for num in range(2, natural_number + 1):
        quotient, remainder = divmod(natural_number, num)
        if not remainder:
            prime_factor_list.append(num)

            # if product of list is equal to the number passed in, we have calculated
            # all prime factors, so return resultant list
            if reduce(operator.mul, prime_factor_list) == natural_number:
                return prime_factor_list

            # Otherwise, we need to process next numbers so use a recursive
            # call to this function with quotient value
            prime_factor_list.extend(prime_factors(quotient))

            # if product of list is equal to the number passed in, we have calculated
            # all prime factors, but at this stage we are in a recursive loop so break out
            if reduce(operator.mul, prime_factor_list) == natural_number:
                break

    return prime_factor_list
