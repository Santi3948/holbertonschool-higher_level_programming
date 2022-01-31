#!/usr/bin/python3
"""10. Square #1


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
        BaseGeometry.integer_validator("width", width)
        BaseGeometry.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string


class Square(Rectangle):
    """class Square


    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
