'''
File: zoo.py
Description: Zoo (manages all animals, staff, enclosures)
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''
import animal
from animal import Animal
from enclosure import Enclosure


class Zoo:
    def __init__(self):
        self.__animals = []
        self.__staff = []
        self.__enclosure = []

    def add_animal(self, animal):
        isinstance(animal, Animal)
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"{animal} added to the zoo")

    def remove_animal(self, animal):
        isinstance(animal, Animal)
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal} removed from the zoo")

    def add_enclosure(self, enclosure):
        isinstance(enclosure, Enclosure)
        if enclosure not in self.__enclosure:
            self.__enclosure.append(enclosure)
            print(f"{enclosure} added to the zoo")

    def remove_enclosure(self, enclosure):
        isinstance(enclosure, Enclosure)
        if enclosure in self.__enclosure:
            self.__enclosure.remove(enclosure)
            print(f"{enclosure} removed from the zoo")

    def add_staff(self, staff):
        if staff not in self.__staff:
            self.__staff.append(staff)
            print(f"{staff} enrolled to the zoo")

    def remove_staff(self, staff):
        if staff in self.__staff:
            self.__staff.remove(staff)
            print(f"{staff} removed from the zoo")

    def assign_animal(self, animal, enclosure):
        enclosure.add_animal(animal)

    def assign_staff_to_animal(self, staff, animal):
        staff.add_animal(animal)

    def assign_staff_to_enclosure(self, staff, enclosure):
        staff.add_enclosure(enclosure)

    def daily_routine(self):
        pass

    def generate_report(self):
        pass

    def get_animals(self):
        return self.__animals

    def get_staff(self):
        return self.__staff

    def get_enclosure(self):
        return self.__enclosure

    zoo_animals = property(get_animals)
    staff = property(get_staff)
    enclosure = property(get_enclosure)
