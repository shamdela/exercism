#!/usr/bin/env python

"""
leap.py

Python script for the Python "Leap", 'exercism' exercise.
A program that will take a year and report if it is a leap year.

Created by: shamdela
Date:       15/09/2016
"""

def is_leap_year(year=None):
    # if a year is evenly divisible by 4
    # except a year that is evenly divisible by 100
    # unless the year is also evenly divisible by 400

    if year and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False
