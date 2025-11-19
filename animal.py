'''
File: filename.py
Description: animal file
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy."
'''


class Animal:
    def __init__(self, name, species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__animal = []

    def add_animal(self, animal):
        if animal not in self.__animal:
            self.__animal.append(animal)
            print(f"{animal} added")

    def remove_animal(self, animal):
        if animal in self.__animal:
            self.__animal.remove(animal)
            print(f"{animal} removed")

    def sound(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass



