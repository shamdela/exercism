#!/usr/bin/env python

"""
space_age.py

Python script for the Python "Space Age", 'exercism' exercise.

A program that, given an age in seconds, calculates how old someone is in terms of a given planet's solar years.

Created by: shamdela
Date:       03/11/2016
"""
EARTH_DAYS_ORB_PERIOD = 365.25
MERCURY_ORB_PERIOD = 0.2408467
VENUS_ORB_PERIOD = 0.61519726
MARS_ORB_PERIOD = 1.8808158
JUPITER_ORB_PERIOD = 11.862615
SATURN_ORB_PERIOD = 29.447498
URANUS_ORB_PERIOD = 84.016846
NEPTUNE_ORB_PERIOD = 164.79132


class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round(self.seconds / 60 / 60 / 24 / EARTH_DAYS_ORB_PERIOD, 2)

    def on_mercury(self):
        return round(self.on_earth() / MERCURY_ORB_PERIOD, 2)

    def on_venus(self):
        return round(self.on_earth() / VENUS_ORB_PERIOD, 2)

    def on_mars(self):
        return round(self.on_earth() / MARS_ORB_PERIOD, 2)

    def on_jupiter(self):
        return round(self.on_earth() / JUPITER_ORB_PERIOD, 2)

    def on_saturn(self):
        return round(self.on_earth() / SATURN_ORB_PERIOD, 2)

    def on_uranus(self):
        return round(self.on_earth() / URANUS_ORB_PERIOD, 2)

    def on_neptune(self):
        return round(self.on_earth() / NEPTUNE_ORB_PERIOD, 2)

