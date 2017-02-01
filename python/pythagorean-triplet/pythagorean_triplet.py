#!/usr/bin/env python

"""
pythagorean_triplet.py

Python script for the "Pythagorean Triplet", 'exercism' exercise.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
A script to find ind the product a * b * c..

Created by: shamdela
Date:       22/12/2016
"""
from math import gcd


def primitive_triplets(b):
    """ Takes a value 'b', that must be divisible by 4.

    :param b:
    :return: Set of triplets that are primitive pythagorean triplets having b as one of their components
    """
    if b % 4 != 0:
        raise ValueError

    triplets = set()
    n = 1
    while b >= 2 * n * n:
        m, r = divmod(b, 2 * n)
        if not r and m > n > 0:
            if coprime(m, n) and not (odd(m) and odd(n)):
                a = m ** 2 - n ** 2
                c = m ** 2 + n ** 2
                tuple_triplet = tuple(sorted([a, b, c]))
                if is_triplet(tuple_triplet):
                    triplets.add(tuple_triplet)
        n += 1
    return triplets


def triplets_in_range(min, max):
    """ Takes min and max params and loops through values in this range to find a set of pythagorean
    triplets.
    Formula for generating Pythagorean triples:
    a=(m^2-n^2), b=2*m*n and c=(m^2+n^2)

    :param min: Minimum range value
    :param max: Maximum range value
    :return: Set of triplets that are in specified range
    """
    py_triplet_list = list()
    for x in range(min, max + 1):
        for y in range(x + 1, max + 1):
            for z in range(y + 1, max + 1):
                if is_triplet((x,y,z)):    # See Pythagorean triplet formula
                    py_triplet_list.append(tuple(sorted((y, z, x))))
    return set(py_triplet_list)


def is_triplet(triplet):
    """ Takes a 3 valued tuple as argument and checks that one of these tuple values is divisible by 4.
    Returns False is this condition is not met.

    :param triplet: A tuple with values a, b and c
    :return: Boolean
    """
    a, b, c = sorted(triplet)
    return a*a + b*b == c*c


def coprime(a, b):
    """ Takes 2 values a and b, and uses gcd function from math module to return a boolean if the gcd == 1

    :param a:
    :param b:
    :return: Boolean
    """
    return gcd(a, b) == 1


def odd(n):
    """ Takes an int value and checks if it is odd.

    :param n: An integetr value
    :return: Boolean
    """
    return n % 2 != 0
