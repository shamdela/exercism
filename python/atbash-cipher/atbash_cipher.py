#!/usr/bin/env python

"""
atbash_cipher.py

Python script for the Python "Atbash Cipher", 'exercism' exercise.

An implementation of the atbash cipher, an ancient encryption system created in the Middle East.

Created by: shamdela
Date:       13/10/2016
"""
import re

PLAIN ='abcdefghijklmnopqrstuvwxyz'
CIPHER = 'zyxwvutsrqponmlkjihgfedcba'
translator = str.maketrans(PLAIN, CIPHER)


def decode(cipher):
    '''
    Converts text to lowercase first, and then translates it based on translator. Then removes any spaces.
    :param cipher:
    :return decoded cipher string:
    '''
    return cipher.lower().translate(translator).replace(" ", "")


def encode(plain):
    '''
    Runs a regex on string to match characters and uses lowercase version of text, and then translates it based on
    translator.
    :param plain:
    :return :decoded cipher string
    '''
    plain = re.sub(r'[^\w]', '', plain)
    cipher = plain.lower().translate(translator)
    ciphered_string = ""

    for i in range(len(cipher)):
        if i % 5 == 0 and i > 0:
            ciphered_string += " "
        ciphered_string += cipher[i]

    return ciphered_string
