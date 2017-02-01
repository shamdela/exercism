#!/usr/bin/env python

"""
robot_simulator.py

Python script for the Python "Robot Simulator", 'exercism' exercise.

A program that represents a robot simulator. A robot factory's test facility needs a program to verify robot movements.

Created by: shamdela
Date:       10/10/2016
"""


class NORTH:

    @staticmethod
    def turn_left():
        return WEST

    @staticmethod
    def turn_right():
        return EAST

    @staticmethod
    def advance(x, y):
        return x, y + 1


class SOUTH:

    @staticmethod
    def turn_left():
        return EAST

    @staticmethod
    def turn_right():
        return WEST

    @staticmethod
    def advance(x, y):
        return x, y - 1


class EAST:
    @staticmethod
    def turn_left():
        return NORTH

    @staticmethod
    def turn_right():
        return SOUTH

    @staticmethod
    def advance(x, y):
        return x + 1, y


class WEST:

    @staticmethod
    def turn_left():
        return SOUTH

    @staticmethod
    def turn_right():
        return NORTH

    @staticmethod
    def advance(x, y):
        return x - 1, y


class Robot:

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = (x, y)

    def turn_left(self):
        self.bearing = self.bearing.turn_left()

    def turn_right(self):
        self.bearing = self.bearing.turn_right()

    def advance(self):
        self.coordinates = self.bearing.advance(self.coordinates[0], self.coordinates[1])

    def simulate(self, instructions):
        for instruction in instructions:
            if instruction == 'R':
                self.turn_right()
            elif instruction == 'L':
                self.turn_left()
            else:
                self.advance()

