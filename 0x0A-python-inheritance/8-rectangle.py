#!/usr/bin/python3
"""
8. Rectangle
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0" .format(name))


class Rectangle(BaseGeometry):
    """
    class Rectangle
    """

    def __init__(self, width, height):
        """
        init
        """
        super().integer_validator(self, "width", width)
        super().integer_validator(self, "height", height)
        self.__width = width
        self.__height = height
