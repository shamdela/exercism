#!/usr/bin/env python

"""
simple_cipher.py

Python script for the "Simple Cipher", 'exercism' exercise.
A program that implements a simple shift cipher like Caesar and
a more secure substitution cipher

Created by: shamdela
Date:       16/11/2016
"""
import re, string, random

ALPHABET = string.ascii_lowercase
MIN_KEY_LEN = 100
MAX_KEY_LEN = 110

class Caesar:
    """ A class representing a simple shift cipher like Caesar
    """
    def __init__(self):
        self.cipher = 'defghijklmnopqrstuvwxyzabc'

    def encode(self, message):
        message = re.sub(r'[0-9\W]', '', message)               # substitute out digits and whitespace
        translator = str.maketrans(ALPHABET, self.cipher)
        return message.lower().translate(translator)

    def decode(self, cipher):
        translator = str.maketrans(self.cipher, ALPHABET)
        return cipher.translate(translator)


class Cipher:
    """ A class representing a a more secure substitution cipher
    """
    def __init__(self, key=None):
        if not key:
            self.key = self.generate_random_key()
        else:
            if bool(re.search(r'[\dA-Z]', key)):
                raise ValueError
            shift = ord(key[0]) - ord('a')
            self.key = ALPHABET[shift:] + ALPHABET[:shift]

    def encode(self, message):
        message = re.sub(r'[0-9\W]', '', message)  # substitute out digits and whitespace
        translator = str.maketrans(ALPHABET, self.key)
        return message.translate(translator)

    def decode(self, cipher):
        translator = str.maketrans(self.key, ALPHABET)
        return cipher.translate(translator)

    def generate_random_key(self):
        return ''.join(random.sample(ALPHABET * 5, random.randint(MIN_KEY_LEN, MAX_KEY_LEN)))


