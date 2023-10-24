#!/usr/bin/python3
"""
This module defines a class Square
"""


class Square:
    """
    A class to represent a square
    """

    def __init__(self, size=0):
        """
        Initializes a new Square

        Args:
            size (int): The size of the new square.

        Raises:
            TypeError: If `size` is not an integer or a float.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """
        Getter for the private instance attribute `size`.

        Returns:
            The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the private instance attribute `size`.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If `value` is not an integer or a float.
            ValueError: If `value` is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares the area of two squares.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the two squares is equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares the area of two squares.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the two squares is not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Compares the area of two squares.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the first square is less than the area of the second square,
            False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares the area of two squares.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the first square is less than or equal to the area of the second square,
            False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Compares the area of two squares.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the first square is greater than the area of the second square,
            False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares the area of two squares.

        Args:
            other (Square): The other square.

        Returns:
            True if the area of the first square is greater than or equal to the area of the second square,
            False otherwise.
        """
        return self.area() >= other.area()
