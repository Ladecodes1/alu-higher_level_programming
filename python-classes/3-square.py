#!/usr/bin/python3

"""
Module documentation:
This module defines a Square class with a private instance attribute `size`,
size validation, and a method to calculate the area.
"""


class Square:
    """
    Class documentation:
    This class defines a square with a private instance attribute `size`,
    size validation, and a method to calculate the area.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with a private size attribute.

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
