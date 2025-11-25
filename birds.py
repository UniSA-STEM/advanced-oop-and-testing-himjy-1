'''
File: birds.py
Description: Defines the Bird subclass of Animal.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    """
    Birds inherit shared attributes and behaviours from the Animal class.
    This class implements the abstract methods defined in Animal:
    - sound()
    - eat()
    - sleep()
    """

    def sound(self):
        """
        Print the sound a bird makes.
        """
        print("Bird sound")

    def eat(self):
        """
        Print how the bird eats.
        """
        print("Bird is eating")

    def sleep(self):
        """
        Print how the bird sleeps.
        """
        print("Bird is sleeping")