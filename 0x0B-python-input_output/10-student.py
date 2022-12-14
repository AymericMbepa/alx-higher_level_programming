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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation of a Student instance"""
        if attrs is None:
            return self.__dict__
        return {key: value for (key, value) in self.__dict__.items()
                if key in attrs}
