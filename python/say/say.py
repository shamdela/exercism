#!/usr/bin/env python

"""
say.py

Python script for the Python "Say", 'exercism' exercise.

A program that will take a number from 0 to 999,999,999,999 and spell out that number in English.

Created by: shamdela
Date:       19/10/2016
"""
import collections

zero_19 = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
             9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
             16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}

tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

large_numbers = {100: "hundred", 1000: "thousand", 1000000: "million", 1000000000: "billion"}


def say(number):
    """
    A function that takes a number and converts it to text, returning its English text version.
    :param number:
    :return:
    """
    try:
        number_text = ""    # A string holder for the text

        # For numbers less than 20
        if number < 20:
            return zero_19[number]

        # For numbers less than 100
        if number < 100:
            number, rem = divmod(number, 10)
            ordered_tens_dict = collections.OrderedDict(sorted(tens.items(), key=lambda t: t[0]))
            number_text += list(ordered_tens_dict.values())[number - 2]
            if rem > 0:
                number_text += '-' + zero_19[rem]
            return number_text

        # For numbers less than 1000
        if number < 1000:
            number, rem = divmod(number, 100)
            number_text += zero_19[number] + ' ' + large_numbers[100]
            if rem > 0:
                number_text += ' and ' + say(rem)   # recursive call with remainder
            return number_text

        # For numbers greater than 1000
        num_list = []
        # break number up into chunks of thousands.
        # So `1234567890` should yield a list like 1, 234, 567, and 890,
        while number != 0:
            number, rem = divmod(number, 1000)
            num_list.insert(0, rem)

        index = len(num_list) - 1
        ordered_num_dict = collections.OrderedDict(sorted(large_numbers.items(), key=lambda t: t[0]))

        for i in num_list:
            if index > 0 and i > 0:
                number_text += ' ' + say(i)     # recursive call with remainder
                number_text += ' ' + list(ordered_num_dict.values())[index]
            elif i > 0:
                if i < 20:
                    number_text += ' and'
                number_text += ' ' + say(i)     # recursive call with remainder
            index -= 1

        return number_text.lstrip()

    except Exception:
        raise AttributeError("Value out of range: {}. Only 0-999,999,999,999 permitted".format(number))
