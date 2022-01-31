#!/usr/bin/python3
"""9. Full rectangle


"""


class BaseGeometry:
    """BaseGeometry class


    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{:s} must be an integer" .format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0" .format(name))


class Rectangle(BaseGeometry):
    """class Rectangle


    """

    def __init__(self, width, height):
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string