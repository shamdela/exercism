#!/usr/bin/env python

"""
sieve.py

Python script for the Python "Sieve", 'exercism' exercise.

A program that uses the Sieve of Eratosthenes to find all the primes from 2 up to a given number.

Created by: shamdela
Date:       12/10/2016
"""


def sieve(limit):
    '''
    Loop through range from 2 to limit number and check if number is a prime number
    If its a prime number, add to list
    :param limit:
    :return list of numbers that meet criteria of being not prime:
    '''
    return [num for num in range(2, limit + 1) if not is_prime(num)]


def is_prime(num):
    '''
    Check if num passed in is a prime number
    :param num:
    :return list of prime numbers:
    '''
    return [num for integer in range(2, num) if num % integer == 0]
