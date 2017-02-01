#!/usr/bin/env python

"""
etl.py

Python script for the Python "Etl", 'exercism' exercise.

A program that, will `Transform` step of an Extract-Transform-Load.
Extract-Transform-Load (ETL) is a fancy way of saying, "We have some crufty, legacy data over in this system,
and now we need it in this shiny new system over here, so we're going to migrate this."

Created by: shamdela
Date:       09/11/2016
"""


def transform(old_dict):
    """
    We read in an old dictionary where each value can be a list of items. We transform these then into a
    new list where each item in the old list are the keys in the new dictionary.
    :param old_dict:
    :return: new_dictionary: with each value from old, acting as a key, in the new dictionary
    """
    return {item.lower(): key for key, value in old_dict.items() for item in value}
