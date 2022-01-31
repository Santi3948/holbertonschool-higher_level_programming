#!/usr/bin/python3
"""11. Square #2
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square
    """

    def __init__(self, size):
        """
        init
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        area
        """
        return self.__size * self.__size

    def __str__(self):
        """
        str
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
