'''
File: reptiles.py
Description: Defines the Reptile subclass of Animal.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

import environment
from animal import Animal

class Reptile(Animal):
    """
    Reptiles implement the abstract methods inherited from Animal:
        - sound()
        - eat()
        - sleep()
    """
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)
        self.__enclosure_type = environment.Type.Wetlands


    # Required abstract method implementations
    def sound(self):

        print("Reptile sound")

    def eat(self):
        print("Reptile eat")

    def sleep(self):
        print("Reptile sleep")

    def get_enclosure_type(self):
        return self.__enclosure_type

    