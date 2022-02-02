#!/usr/bin/python3
"""
10. Student to JSON with filter
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance
        """
        dic = {}
        if type(attrs) is list:
            for key in attrs:
                if type(key) != str:
                    return self.__dict__
                if key in self.__dict__:
                    dic[key] = self.__dict__[key]
            return dic
        else:
            return self.__dict__
