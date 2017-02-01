#!/usr/bin/env python

"""
circular_buffer.py

Python script for the "Circular Buffer", 'exercism' exercise.
An implementation of a data structure that uses a single, fixed-size buffer as if it were
connected end-to-end.

Created by: shamdela
Date:       23/12/2016
"""


class CircularBuffer:
    """ A class representing a Circular Buffer data structure. It will use a list data structure to
    implement a queueing mechanism """
    def __init__(self, buffer_length):
        self.buffer_length = buffer_length  # fixed size of queue
        self.buffer = []                    # a list representing our 'Circular Buffer' data structure

    def write(self, element):
        if self.is_full():
            raise BufferFullException
        self.buffer.insert(0, element)  # Insert element at start of queue

    def read(self):
        if self.is_empty():
            raise BufferEmptyException
        return self.buffer.pop()        # Pop last element off queue

    def clear(self):
        self.buffer = []

    def overwrite(self, element):
        # If queue is not empty and is full, pop oldest item off
        if not self.is_empty() and self.is_full():
            self.buffer.pop()
        self.buffer.insert(0, element)  # Insert element at start of queue

    def is_empty(self):
        return self.buffer == []

    def is_full(self):
        return self.buffer_length == len(self.buffer)


class BufferFullException(Exception):
    """ Raise when Buffer is full """


class BufferEmptyException(Exception):
    """ Raise when Buffer is empty """