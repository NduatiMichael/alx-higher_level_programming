#!/usr/bin/python3
"""This module defines a Square class"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize a new Square instance"""
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square using '#' characters"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print("#" * self.__size)
