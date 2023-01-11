#!/usr/bin/python3
"""creating a class"""


class Square:
    """class for square"""
    def __init__(self, size=0):
        """constructor"""
        if type(size) is int:
            raise TypeError ("size must be an integer")
        if size < 0:
            raise ValueError ("size must be >= 0")
        self.__size = size
