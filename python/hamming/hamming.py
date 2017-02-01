#!/usr/bin/env python

"""
hamming.py

Python script for the Python "Hamming", 'exercism' exercise.
Implementation of a program that can calculate the Hamming difference between two DNA strands.

Created by: shamdela
Date:       19/09/2016
"""


def distance(dna1, dna2):
    return len([a for a, b in zip(dna1, dna2) if a != b])


