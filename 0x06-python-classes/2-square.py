#!/usr/bin/python3
"""This module defines a square based on 1-square.py

   It implements value and type checks for its attributes
"""


class Square:
    """square implementation"""
    def __init__(self, size=0):
        """Type checks for attributes"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
