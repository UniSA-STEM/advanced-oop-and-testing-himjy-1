'''
File: mammals.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''
import environment
from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)
        self.__enclosure_type = environment.Type.Savannah

    def sound(self):
        print("Mammal sound")

    def eat(self):
        print("Mammal eat")

    def sleep(self):
        print("Mammal sleep")

    def get_enclosure_type(self):
        return self.__enclosure_type

    mammal_enclosure = property(get_enclosure_type)



