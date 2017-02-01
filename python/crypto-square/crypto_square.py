#!/usr/bin/env python

"""
crypto_square.py

Python script for the "Crypto Square", 'exercism' exercise.
A program that given an English text, outputs the encoded version
of that text.

Created by: shamdela
Date:       29/11/2016
"""
import re, math


def encode(text):
    normalised = normalise(text)


def normalise(text):
    return re.sub(r"[^\w]", "", text.lower())
