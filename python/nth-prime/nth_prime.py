#!/usr/bin/env python

"""
nth_prime.py

Python script for the "Nth Prime", 'exercism' exercise.
A program that can tell you what the nth prime is

Created by: shamdela
Date:       18/01/2017
"""


def nth_prime(n):
    """ Takes a number and checks its n index in prime numbers list

    :param n:
    :return: nth prime number in the list
    """
    prime_number_list = [2]             # intitialise list with 2 as its first prime number
    index = 3                           # start the index at 3
    while len(prime_number_list) < n:   # loop until we have a list with n prime numbers
        if is_prime(index):
            prime_number_list.append(index)
        index += 1
    return prime_number_list[n - 1]


def is_prime(number):
    """ Takes a number, and returns True if its a prime number, False otherwise

    :param number:
    :return: True or False if a number is a prime number
    """
    for num in range(3, number):                   # Start looping from 3 up to the number, as we know 2 is prime
        if number % num == 0 or number % 2 == 0:   # If number is divisble by another number its not prime
            return False                           # We also check if its divisble by 2 here as we started looping at 3
    return True
