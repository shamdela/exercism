#!/usr/bin/env python

"""
roman_numerals.py

Python script for the Python "Roman Numerals", 'exercism' exercise.

A program that contains a function to convert from normal numbers to Roman Numerals.

Created by: shamdela
Date:       27/10/2016
"""
# Romans Numerals are based on the following symbols:
ROMAN_SYMBOLS = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}

# Romans Numerals can be combined in these combinataions
ROMAN_COMBINATIONS = {0: "", 1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
                    10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
                   100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM"}


def numeral(arabic):
    """
    A function to take in an integer and convert to Roman Numerals

    :param arabic: The integer to be converted into Roman Numerals
    :return: The Roman numeral
    """
    if arabic in ROMAN_SYMBOLS:
        return ROMAN_SYMBOLS[arabic]

    if arabic in ROMAN_COMBINATIONS:
        return ROMAN_COMBINATIONS[arabic]

    if arabic > 1000:
        thousands, hundreds, tens, ones = str(arabic)  # unpack integer into componenets
        return (ROMAN_SYMBOLS[1000] * int(thousands)) + ROMAN_COMBINATIONS[int(hundreds) * 100] + \
                    ROMAN_COMBINATIONS[int(tens) * 10] + ROMAN_COMBINATIONS[int(ones)]

    if arabic > 100:
        hundreds, tens, ones = str(arabic)  # unpack integer into componenets
        return ROMAN_COMBINATIONS[int(hundreds) * 100] + ROMAN_COMBINATIONS[int(tens) * 10] + ROMAN_COMBINATIONS[int(ones)]

    if arabic > 10:
        tens, ones = str(arabic)  # unpack integer into componenets
        return ROMAN_COMBINATIONS[int(tens) * 10] + ROMAN_COMBINATIONS[int(ones)]
