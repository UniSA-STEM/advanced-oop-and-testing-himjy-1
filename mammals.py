'''
File: mammals.py
Description: Defines the Mammal subclass of Animal.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

import environment
from animal import Animal

class Mammal(Animal):
    """
    Mammals inherit all shared functionality from the Animal base class
    """

    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)
        self.__enclosure_type = environment.Type.Savannah

    # Required abstract method implementations
    def sound(self):
        print("Mammal sound")

    def eat(self):
        print("Mammal eat")

    def sleep(self):
        print("Mammal sleep")

    # Enclosure getter
    def get_enclosure_type(self):
        return self.__enclosure_type

    # Property
    mammal_enclosure = property(get_enclosure_type)



