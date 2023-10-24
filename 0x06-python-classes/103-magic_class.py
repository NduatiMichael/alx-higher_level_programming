#!/usr/bin/python3
"""
This module defines a Singly linked list
"""


import math


class MagicClass:
    """square implementation"""
    def __init__(self, radius=0):
        """defines self and radius"""
        self.__radius = 0
        self.radius = radius

    @property
    def radius(self):
        """sets the radius"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """sets the radious"""
        if type(value) not in [int, float]:
            raise TypeError('radius must be a number')
        if value < 0:
            raise ValueError('radius must be >= 0')
        self.__radius = value

    def area(self):
        """This function calculates area"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """This function calculates circumference"""
        return 2 * math.pi * self.__radius
