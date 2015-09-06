#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Week 1 Assignment 1 Part 1"""


def listDivide(numbers, divide=2):
    """A function that returns the number of elements in the numbers list that
    are divisible by divide.

    Args:
        numbers (list): A list of numbers.
        divide (int): A parameter used for division. By default set to 2.

    Returns:
        The number of elements in the numbers list that are divisble by divide.

    Examples:
        >>> print listDivide([1,2,3,4,5,6,7],)
        3

        >>> print listDivide([11,22,33,45,67,89,12345], 11)
        3
    """

    i = 0
    for element in numbers:
        if element % divide == 0:
            i += 1
    return i


class ListDivideException:
    """A custom exception."""

    def __init__(self, message="There seems to be an error."):
        """Error message raised when there is an error in the listDivide
        function."""

        self.message = message
        print message


def testListDivide():
    """A function to test the listDivide."""
    try:
        listDivide([1, 2, 3, 4, 5])  # should result in 2
        listDivide([2, 4, 6, 8, 10])  # should result in 5
        listDivide([30, 54, 63, 98, 100], divide=10)  # should result in 2
        listDivide([])  # should result in 0
        listDivide([1, 2, 3, 4, 5], 1)  # should result in 5
    except:
        ListDivideException()


if __name__ == '__main__':
    testListDivide()
