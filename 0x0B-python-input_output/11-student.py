#!/usr/bin/python3
"""
11. Student to disk and reload
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

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance
        """
        for key in dict(self.__dict__):
            if key in json:
                self.__dict__[key] = json[key]
