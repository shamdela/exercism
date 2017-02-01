#!/usr/bin/env python

"""
saddle_points.py

Python script for the "Saddle Points", 'exercism' exercise.
A program that detects saddle points in a matrix. A "saddle point" is x,y coord that is greater than or equal to
every element in its row and the less than or equal to every element in its column

Created by: shamdela
Date:       18/01/2017
"""


def saddle_points(matrix):
    """ Takes a 2d list (matrix) and returns a set of valid saddle points

    :param matrix:
    :return: A set of saddle points (x,y coords)
    """
    return


if __name__ == '__main__':
    #set([(1, 0)])
    inp = [[9, 8, 7], [5, 3, 2], [6, 6, 7]]
    print(saddle_points(inp))
