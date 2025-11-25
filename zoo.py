'''
File: zoo.py
Description: Manages all animals, staff, and enclosures in the zoo.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from enclosure import Enclosure
from zookeeper import Zookeeper
from veterinarian import Veterinarian

class Zoo:
    """
    The Zoo class acts as the central manager for animals, enclosures, and staff.

    Responsibilities include:
        - Adding and removing animals
        - Adding and removing staff
        - Adding and removing enclosures
        - Assigning animals to enclosures
        - Assigning staff to animals
        - Performing the daily routine (feeding, cleaning, medical checks)
    """

    def __init__(self):
        "empty zoo"
        self.__animals = []
        self.__staff = []
        self.__enclosure = []

    def add_animal(self, animal):
        """Add an Animal to the zoo."""
        isinstance(animal, Animal)
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"{animal} added to the zoo")

    def remove_animal(self, animal):
        """Remove an Animal from the zoo."""
        isinstance(animal, Animal)
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal} removed from the zoo")

    def add_enclosure(self, enclosure):
        """Add an Enclosure to the zoo."""
        isinstance(enclosure, Enclosure)
        if enclosure not in self.__enclosure:
            self.__enclosure.append(enclosure)
            print(f"{enclosure} added to the zoo")

    def remove_enclosure(self, enclosure):
        """Remove an Enclosure from the zoo."""
        isinstance(enclosure, Enclosure)
        if enclosure in self.__enclosure:
            self.__enclosure.remove(enclosure)
            print(f"{enclosure} removed from the zoo")

    def add_staff(self, staff):
        """Add a staff member to the zoo."""
        if staff not in self.__staff:
            self.__staff.append(staff)
            print(f"{staff} enrolled to the zoo")

    def remove_staff(self, staff):
        """Remove a staff member from the zoo."""
        if staff in self.__staff:
            self.__staff.remove(staff)
            print(f"{staff} removed from the zoo")

    def assign_animal(self, animal, enclosure):
        """Assign an animal to an enclosure."""
        enclosure.add_animal(animal)
        print(f"Assigned {animal.animal_name} to {enclosure.name} enclosure")

    def assign_staff_to_animal(self, staff, animal):
        """Assign staff to an animal (Zookeeper or Veterinarian)."""
        staff.add_animal(animal)
        print(f"Assigned {staff.name} to the {animal.name}")

    def assign_staff_to_enclosure(self, staff, enclosure):
        """Assign staff to an enclosure"""
        staff.add_enclosure(enclosure)
        print(f"Assigned {staff.name} to {enclosure.name} enclosure")

    def daily_routine(self):
        """
        Run the daily routine for all staff
        """
        for staff in self.__staff:
            if isinstance(staff, Zookeeper):
                staff.task()
                staff.clean()
            elif isinstance(staff, Veterinarian):
                staff.task()
                staff.heal()

    # getters and properties
    def get_animals(self):
        return self.__animals

    def get_staff(self):
        return self.__staff

    def get_enclosure(self):
        return self.__enclosure

    zoo_animals = property(get_animals)
    staff = property(get_staff)
    enclosure = property(get_enclosure)
