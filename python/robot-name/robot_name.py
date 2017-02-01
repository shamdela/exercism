#!/usr/bin/env python

"""
robot_name.py

Python script for the "Robot Name", 'exercism' exercise.
An implementation of a program that manages robot factory settings

Created by: shamdela
Date:       12/01/2017
"""
import random
import string


class Robot:
    """ A class representing a Robot. It's only property is a name.
    """
    def __init__(self):
        """ On initialisation, a random name is generated """
        self.name = self.generate_name()

    def reset(self):
        """ Reset robot so that it's name gets wiped. Repeat name generation until the
        generated name is not the same as previous name
        """
        while self.generate_name() == self.name:
            self.name = self.generate_name()

    @staticmethod
    def generate_name():
        """ Use random module to generate a name in the format of two uppercase letters
        followed by three digits
        """
        letters = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
        digits = random.choice(string.digits) + random.choice(string.digits) + random.choice(string.digits)
        return letters + digits
