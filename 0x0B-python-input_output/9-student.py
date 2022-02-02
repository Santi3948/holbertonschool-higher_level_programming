#!/usr/bin/python3
"""
9. Student to JSON
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Instantiation with first_name, last_name and age
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance
        """
        return self.__dict__
