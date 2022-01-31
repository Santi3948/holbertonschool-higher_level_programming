#!/usr/bin/python3
"""11. Square #2
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square


    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        string = "[Square] " + str(self.__width) + "/" + str(self.__height)
        return string
