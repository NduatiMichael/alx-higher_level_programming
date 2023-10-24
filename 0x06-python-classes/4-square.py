#!/usr/bin/python3
"""This module contains a Square class"""


class Square:
    """This class implements square attributes"""

    def __init__(self, size=0):
        """Initializes a square"""
        self.size = size

    @property
    def size(self):
        """Returns the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square"""
        return self.__size ** 2
