#!/usr/bin/env python

"""
gigasecond.py

Python script for the Python "Gigsecond", 'exercism' exercise.
Implementation of a program that that calculates the moment when someone has lived for 10^9 seconds.
A gigasecond is 10^9 (1,000,000,000) seconds.

Created by: shamdela
Date:       20/09/2016
"""
from datetime import timedelta


def add_gigasecond(test_time):
    return test_time + timedelta(seconds=1000000000)
