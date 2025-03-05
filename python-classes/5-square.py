#!/usr/bin/python3

"""
Module documentation:
This module defines a Square class with a private instance attribute `size`,
a getter and setter for `size`, a method to calculate the area, and a method
to print the square using the `#` character.
"""


class Square:
    """
    Class documentation:
    This class defines a square with a private instance attribute `size`,
    a getter and setter for `size`, a method to calculate the area, and a method
    to print the square using the `#` character.
    """

    def __init__(self, size=0):
        """
        Initialize a Square instance with a private size attribute.

        Args:
            size (int, optional): The size of the square. Defaults to 0.
        """
        self.size = size  # Use the setter to validate the size

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Print the square using the `#` character.

        If size is 0, print an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
