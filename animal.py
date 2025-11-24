'''
File: animal.py
Description: animal file
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy."
'''
from abc import ABC, abstractmethod

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

    # sound is an abstract method because it forces every subclass
    # (Mammal, Reptile, Bird) to implement their own version of sound().
    # This enables polymorphism.
    # The animal class is the base class/parent class of the subclass/child class (Mammal, Reptile, Bird)

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

    def sick(self, amount):
        self.__health -= amount
        print(f"{self.animal_name} is sick: Health {self.__health}")

    def heal(self, amount):
        self.__health += amount
        if self.__health > 100:
            self.__health = 100


    def feed(self):
        self.__hunger = False

    def __str__(self):
        return self.__name

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

    animal_name = property(get_name)
    species = property(get_species)
    age = property(get_age)
    diet = property(get_diet)
    hunger = property(get_hunger)
    health = property(get_health)





