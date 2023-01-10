#!/usr/bin/python3
"""
 class Student that defines a studen

"""


class Student:
    """that defines a student"""

    def __init__(self, first_name, last_name, age):
        """init methof sor student class

        Args:
           first_name: student first_name
           last_name: student last_name
           age: student age
        """
        self.__first_name = first_name
        self.__last_name = last_name
        self._age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student instance"""
        return {key: value for (key, value) in self.__dict__.items()
                if key in list(self.__dict__.keys())}
