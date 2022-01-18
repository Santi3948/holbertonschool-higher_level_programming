#!/usr/bin/python3
class Square:
    __size = 0

    def size_validation(self, size=0):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")

    def __init__(self, size=0):
        self.size_validation(size)
        self.__size = size
