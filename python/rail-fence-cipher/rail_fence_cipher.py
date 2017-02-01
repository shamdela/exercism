#!/usr/bin/env python

"""
rail_fence_cipher.py

Python script for the "Rail Fence Cipher", 'exercism' exercise.
A script to implement encoding and decoding for the rail fence cipher, which is a form of
transposition cipher that gets its name from the way in which it's encoded.

Created by: shamdela
Date:       14/01/2017
"""


def encode(message, rails):
    """ Takes a message and number of rails to encode

    :param message:
    :param rails: number of rails to use
    :return: encoded message
    """
    counter = 0
    direction = 'FWD'
    encoded_list = [[] for x in range(rails)]       # set up empty 2d list

    # loop through every char in message and add it into the appropriate bucket
    for item in message:
        encoded_list[counter].append(item)

        # calculate the direction and counter
        if direction == 'FWD':
            if counter == rails - 1:    # if we are at last row, change direction and start decrementing counter
                direction = 'BWD'
                counter -= 1
            else:
                counter += 1
        else:
            if counter == 0:            # if we are at first row, change direction and start incrementing counter
                direction = 'FWD'
                counter += 1
            else:
                counter -= 1

    # return string with combined elements from all internal lists
    return "".join(letter for row in encoded_list for letter in row)


def decode(message, rails):
    """ Takes a message and number of rails to decode

    :param message:
    :param rails: number of rails to use
    :return: decoded message
    """
    # set up empty list with same size as length of message
    decoded_str = [""] * len(message)
    pos = 0

    # loop through for number of rails
    for index in range(rails):
        step1 = (rails - 1 - index) * 2                 # step to increment index going forward
        step2 = index * 2                               # step to increment index coming back
        while index < len(message):
            if step1 != 0:                              # index going down
                decoded_str[index] = message[pos]
                pos += 1
                index += step1
            if step2 != 0 and index < len(message):     # index coming back
                decoded_str[index] = message[pos]
                pos += 1
                index += step2

    return "".join(decoded_str)     # return list as string
