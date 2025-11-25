'''
File: zookeeper.py
Description: Defines the Zookeeper subclass of Staff.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff
from environment import Clean_level

class Zookeeper(Staff):
    """
    Zookeepers are responsible for:
        - Feeding animals
        - Cleaning enclosures
        - Supervising assigned animals and enclosures

    """
    def __init__(self, role, first_name, last_name, email):
        super().__init__(role, first_name, last_name, email)
        self.__assigned_animal = []
        self.__assigned_enclosure = []
        self.__responsibilities = ["mammal", "reptile", "birds"]

    def add_animal(self, animal):
        """
          Assign an animal to the zookeeper.
        """
        if animal not in self.__assigned_animal:
            self.__assigned_animal.append(animal)
            print(f"{animal} assigned to Zookeeper")

    def add_enclosure(self, enclosure):
        """
        Assign an enclosure to the zookeeper.
        """
        if enclosure not in self.__assigned_enclosure:
            self.__assigned_enclosure.append(enclosure)
            print(f"enclosure assigned to Zookeeper")

    def responsibility(self):
        """Print the primary responsibilities of a Zookeeper."""
        print("Zookeeper is responsible for feeding the animals and cleaning the enclosure")

    def task(self):
        """
        Feed assigned animals if they are hungry.

        Hunger is determined by the animal.hunger attribute:
            if True, feed animal
            if False animal not hungry
        """
        for animal in self.__assigned_animal:
            if animal.hunger:  # True means the animal is hungry
                print(f"{animal} is hungry. Feeding now...")
                animal.feed()  # feed = sets hunger to False
            else:
                print(f"{animal} is not hungry.")

    def clean(self):
        """
         Clean enclosures assigned to the zookeeper.

         Enclosures are cleaned only if their Clean_level is Dirty or NeedsCleaning.
         """
        for enclosure in self.__assigned_enclosure:
            if enclosure.clean_level == Clean_level.Dirty or enclosure.clean_level == Clean_level.NeedsCleaning:
                print("this enclosure needs cleaning")
                enclosure.clean_enclosure()
                print("enclosure is cleaned")
            else:
                print("enclosure is not dirty")

    # Getters and Properties
    def get_responsibilities(self):
        return self.__responsibilities

    def get_animal(self):
        return self.__assigned_animal

    assigned_animals = property(get_animal)
    zookeeper_responsibility = property(get_responsibilities)

