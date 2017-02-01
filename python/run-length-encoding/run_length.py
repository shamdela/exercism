#!/usr/bin/env python

"""
run_length.py

Python script for the Python "Run Length Encoding", 'exercism' exercise.

Implement run-length encoding and decoding.
Run-length encoding (RLE) is a simple form of data compression, where runs
(consecutive data elements) are replaced by just one data value and count.

Created by: shamdela
Date:       20/09/2016
"""
import re


# A simple function to append ech encoded val to a string
def append_result(result, counter, prev_char):
    if counter > 1:
        result += "" + str(counter) + prev_char
    else:
        result += prev_char
    return result


def encode(str_to_encode):
    result = ""         # A String representing our final result
    prev_char = ""      # A var that holds the previous char in loop
    counter = 0         # A counter for each number of chars

    for i in range(len(str_to_encode)):
        # if its first char in string or the sequence is broken
        if i == 0 or str_to_encode[i] != prev_char:
            if counter > 0:
                result = append_result(result, counter, prev_char)
            counter = 1
        else:
            counter += 1

        prev_char = str_to_encode[i]

    # Call again to display last char to encode
    result = append_result(result, counter, prev_char)

    return result


def decode(str_to_decode):
    result = ""
    matches = re.findall('\d*.', str_to_decode)
    for match in matches:
        *number, letter = match     # unpack digits and letter

        # Conditional expression
        result += (int("".join(number) if number else 1) * letter)

    return result

