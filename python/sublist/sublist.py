#!/usr/bin/env python

"""
sublist.py

Python script for the "Sublist", 'exercism' exercise.
A function to determine if a list is a sublist of another list.

Created by: shamdela
Date:       20/12/2016
"""
SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 1, 2, 3, 4


def check_lists(list1, list2 ):
    """ Takes 2 lists and returns a constant based on:
            SUBLIST = if the first list is contained within the second list,
            SUPERLIST = if the second list is contained within the first list,
            EQUAL = if both lists are contained within each other
            UNEQUAL = if none of these are true.

    :param lista:
    :param listb:
    :return: a constant
    """
    if list1 == list2:
        return EQUAL

    if len(list1) < len(list2):
        if list1:
            return perform_check(list1, list2, SUBLIST)
        return SUBLIST
    else:
        if list2:
            return perform_check(list2, list1, SUPERLIST)
        return SUPERLIST


def perform_check(lista, listb, list_type):
    """ Takes 2 lists and the list type constant.
    :param lista:
    :param listb:
    :param list_type: The SUBLIST or SUPERLIST constant
    :return: The list_type passed in or UNEQUAL if lists don't match
    """
    # get list of indexes in list b where first value in list a occurs.
    indices = [i for i, x in enumerate(listb) if x == lista[0]]

    # loop through each index and check that lista == to the equivalent length of numbers in
    # listb from where the index starts
    for idx, index_val in enumerate(indices):
        if lista == listb[index_val:len(lista) + index_val]:
            return list_type
    return UNEQUAL
