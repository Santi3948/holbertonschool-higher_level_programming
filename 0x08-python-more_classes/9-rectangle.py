#!/usr/bin/python3
"""Area and Perimeter"""


class Rectangle:
    """Class Rectangle"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """constructor method"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width
        type(self).number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2

    def __str__(self):
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                string += str(self.print_symbol)
            if i is not (self.__height):
                string += "\n"
        return string

    def __repr__(self):
        return (type(self).__name__ + "(" + str(self.__width) +
                ", " + str(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if type(rect_1).area(rect_1) == type(rect_2).area(rect_2):
            return rect_1
        if type(rect_1).area(rect_1) < type(rect_2).area(rect_2):
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """square method"""
        if size >= 0:
            return cls(size, size)
