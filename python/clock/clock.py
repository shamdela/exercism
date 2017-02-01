#!/usr/bin/env python

"""
clock.py

Python script for the Python "Clock", 'exercism' exercise.
Implementation of a clock that handles times without dates.

Created by: shamdela
Date:       15/09/2016
"""

class Clock:

    def __init__(self, h, m):
        self.hour = h
        self.min = m
        self.calculate()

    def __str__(self):
        return "%02d:%02d" % (self.hour, self.min)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return str(self) == str(other)
        else:
            return False

    def add(self, minutes):
        self.hour = ((minutes / 60) + self.hour) % 24
        self.min = (self.min + minutes) % 60
        return self

    def calculate(self):
        extra_hours = self.min / 60
        new_hours = (extra_hours + self.hour) % 24

        # Conditional Expression - if condition evaluated first
        # x = true_value if condition else false_value
        self.hour = 24 + new_hours if new_hours < 0 else new_hours
        self.min %= 60


