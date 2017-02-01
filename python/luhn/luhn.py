#!/usr/bin/env python

"""
luhn.py

Python script for the Python "Luhn", 'exercism' exercise.

A program that, can take a number and determine whether or not it is valid per the Luhn formula.

Created by: shamdela
Date:       08/11/2016
"""


class Luhn:
    """ The Luhn formula is a simple checksum formula used to validate a variety of identification numbers,
    such as credit card numbers and Canadian Social Insurance Numbers.

    """
    def __init__(self, number):
        """ Constructor for Luhn class

        :param number: The given number to process

        """
        self.number = number
        self.digit_index = 1    # The digit index to double in the Luhn formula - Eg 1, 3, 5 etc

    def addends(self):
        """ Implementation of Luhn formula. Counting from rightmost digit (which is the check digit) and moving
        left, double the value of every second digit. For any digits that thus become 10 or more, subtract 9 from the
        result.

        :return number_list: A list of numbers after Luhn formula applied

        """
        number_list = []
        for index, number in enumerate(str(self.number)[::-1]):
            if index % 2 == self.digit_index:
                val = int(number) * 2
                if val >= 10:
                    val -= 9
                number_list.append(int(val))
            else:
                number_list.append(int(number))

        return number_list

    def checksum(self):
        """ Calculates the checksum of a given number, per the Luhn formula

        :return: Sum of the digits (after luhn formula applied )

        """
        return sum(self.addends())

    def is_valid(self):
        """ Checks if a given number is valid per the Luhn formula
        If the total(after luhn formula applied ) modulus 10 is congruent to 0, then the number is valid

        :return : boolean

        """
        return self.checksum() % 10 == 0

    @classmethod
    def create(cls, number):
        """ A class method to allow alternative instantiation of Luhn class

        :param number: The given number to process
        :return: New number which is the original number with check digit appended to make
                the number valid per the Luhn formula

        """
        cls.number = number
        cls.digit_index = 0         # The digit index to double in the Luhn formula - Eg 0, 2, 4 etc

        remainder = sum(cls.addends(cls)) % 10

        # "ternary" expression
        return int(str(number) + str(10 - remainder)) if remainder > 0 else int(str(number) + str(0))
