'''
File: animal.py
Description: Defines the abstract Animal class for the Zoo Management System.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

"""
Abstract base class representing an animal in the zoo.

This class defines shared attributes and behaviours that all animals must have.
Subclasses (Mammal, Reptile, Bird, etc.) MUST implement the abstract methods:
- sound()
- eat()
- sleep()

"""

class Animal(ABC):
    def __init__(self, name, species, age, diet):
        self.__name = name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__hunger = True
        self.__health = 100

    @abstractmethod
    def sound(self):
        pass
    """
    Abstract method requiring each subclass to define how the animal sounds.
    Enables polymorphism
    """

    # sound is an abstract method because it forces every subclass
    # (Mammal, Reptile, Bird) to implement their own version of sound().
    # This enables polymorphism.
    # The animal class is the base class/parent class of the subclass/child class (Mammal, Reptile, Bird)

    @abstractmethod
    def eat(self):
        """
             Abstract method requiring each subclass to define how the animal eats.
        """
        pass

    @abstractmethod
    def sleep(self):
        """
             Abstract method requiring each subclass to define how the animal sleeps.
        """
        pass

    def sick(self, amount):
        """
             Reduce the animal's health by a given amount.
        """
        self.__health -= amount
        if self.__health <= 50:
            print(f"{self.animal_name} Health: {self.__health}")

        else:
            print(f"{self.animal_name} Health: {self.__health}")

    def heal(self, amount):
        """
        Increase the animal's health by a given amount.
        """

        self.__health += amount
        if self.__health > 100:
            self.__health = 100


    def feed(self):
        """
        Feed the animal, removing hunger state.
        """

        self.__hunger = False

    def __str__(self):
        """
            Return the animal's name as a string.
        """
        return self.__name


    # Getter Methods (Encapsulation)
    def get_name(self):
        return self.__name

    def get_species(self):
        return self.__species

    def get_age(self):
        return self.__age

    def get_diet(self):
        return self.__diet

    def get_hunger(self):
        return self.__hunger

    def get_health(self):
        return self.__health

    # Properties to Private Attributes
    animal_name = property(get_name)
    species = property(get_species)
    age = property(get_age)
    diet = property(get_diet)
    hunger = property(get_hunger)
    health = property(get_health)





