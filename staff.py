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
    def __init__(self, role, first_name, last_name, email):
        self.__role = role
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
        return (f"Role: {self.role}\n"
                f"Staff: {self.first_name} {self.last_name}\n"
                f"Email: {self.email}\n")

    def get_role(self):
        return self.__role

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_email(self):
        return self.__email

    role = property(get_role)
    first_name = property(get_first_name)
    last_name = property(get_last_name)
    email = property(get_email)


