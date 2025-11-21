'''
File: zoo.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Zoo:
    def __init__(self):
        self.__animals = []
        self.__staff = []

    def add_animal(self, animal):
        isinstance(animal, Animal)
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"{animal} added")

    def remove_animal(self, animal):
        isinstance(animal, Animal)
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal} removed")

    def add_enclosure(self):
        pass

    def remove_enclosure(self):
        pass

    def add_staff(self):
        pass

    def remove_staff(self):
        pass

    def assign_animal(self):
        pass

    def daily_routine(self):
        pass

    def generate_report(self):
        pass

    def get_animals(self):
        return self.__animals

    zoo_animals = property(get_animals)