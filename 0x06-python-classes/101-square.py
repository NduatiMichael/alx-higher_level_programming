#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square instance

        Args:
            size (int): size of the square
            position (tuple): position of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square

        Args:
            value (int): size of the square

        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square

        Args:
            value (tuple): position of the square

        Raises:
            TypeError: if value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not isinstance(value[0], int) or not isinstance(value[1], int) or \
                value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size)

    def __str__(self):
        """Return the string representation of the square"""
        result = ""
        if self.__size == 0:
            result += "\n"
        else:
            for i in range(self.__position[1]):
                result += "\n"
            for i in range(self.__size):
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return result[:-1]
