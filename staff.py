'''
File: staff.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    def __init__(self, first_name, last_name, email):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email

    @abstractmethod
    def task(self):
        pass

    @abstractmethod
    def responsibility(self):
        pass

    def __str__(self):
        return (f"Staff: {self.__first_name} {self.__last_name}\n"
                f"Email: {self.__email}")




