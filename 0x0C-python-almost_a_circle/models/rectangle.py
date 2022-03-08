#!/usr/bin/python3
"""
2. First Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle
    """
    @property
    def width(self):
        """width property"""
        return self.__width

    @property
    def height(self):
        """height property"""
        return self.__height

    @property
    def x(self):
        """x property"""
        return self.__x

    @property
    def y(self):
        """y property"""
        return self.__y

    @width.setter
    def width(self, width):
        """width.setter"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @height.setter
    def height(self, height):
        """height.setter"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @x.setter
    def x(self, x):
        """x.setter"""
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @y.setter
    def y(self, y):
        """y setter"""
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """area doc"""
        return self.__height * self.__width

    def display(self):
        """display"""
        for w in range(self.__y):
            print()
        for i in range(self.__height):
            for z in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """str function"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} \
- {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """update function"""
        if args:
            for i in range(len(args)):
                if i == 0:
                    setattr(self, "id", args[i])
                if i == 1:
                    setattr(self, "width", args[i])
                if i == 2:
                    setattr(self, "height", args[i])
                if i == 3:
                    setattr(self, "x", args[i])
                if i == 4:
                    setattr(self, "y", args[i])
        else:
            for key, value in kwargs.items():
                if key == "id":
                    setattr(self, "id", value)
                if key == "width":
                    setattr(self, "width", value)
                if key == "height":
                    setattr(self, "height", value)
                if key == "x":
                    setattr(self, "x", value)
                if key == "y":
                    setattr(self, "y", value)

    def to_dictionary(self):
        """to_dictionary doc"""
        my_dict = {"id": self.id,
                   "width": self.width,
                   "height": self.height,
                   "x": self.x,
                   "y": self.y}
        return my_dict
