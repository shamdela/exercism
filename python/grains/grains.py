#!/usr/bin/env python

"""
grains.py

Python script for the Python "Grains", 'exercism' exercise.

A program that, calculates the number of grains of wheat on a chessboard given that the number on each square doubles.

Created by: shamdela
Date:       08/11/2016
"""

#  NOTE: My initial attempt commented out. Pasted in chrisguidry's work.


def on_square(square):
    """
    Loops through list and doubles number of grains at each
    :param square: represents the square number on chessboard
    :return grains: the number of grains on current square
    """
    '''
    grains = 1  # number of grains at first square
    for i in range(1, square):
        grains *= 2

    return grains
    '''

    return 2 ** (square - 1)


def total_after(square):
    """
    Loops through list and double number of grains at each, and keeps running total
    :param square: represents the square number on chessboard
    :return total: total sum at the current square
    """
    '''
    grains = 1  # number of grains at first square
    total = 1   # total at first square
    for i in range(1, square):
        grains *= 2
        total += grains

    return total
    '''

    return sum(on_square(i) for i in range(1, square + 1))


