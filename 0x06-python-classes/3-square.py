#!/usr/bin/python3
"""This module calculates the area of a square"""


class Square:
    """This class implements square attributes"""
    def __init__(self, size=0):
        """This function specifies conditions"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """This function calculates the area of the square"""
        return self.__size ** 2
