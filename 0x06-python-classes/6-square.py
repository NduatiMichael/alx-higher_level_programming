#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves the position of the square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square"""

        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of the square"""

        return self.__size ** 2

    def my_print(self):
        """Prints the square"""

        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()
