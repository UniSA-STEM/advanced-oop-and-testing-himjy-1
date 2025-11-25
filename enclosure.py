'''
File: enclosure.py
Description: Defines the Enclosure class for storing and managing animals.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''
import environment
import mammals
import reptiles
import birds


class Enclosure:
    """
    Represents an enclosure within the zoo.

    Each enclosure has:
        - A size (Small, Medium, Large)
        - An environment type (Savannah, Wetlands, Rainforest, etc.)
        - A clean level (Dirty, NeedsCleaning, Clean)
        - A permitted animal type (Mammal, Reptile, Bird)
        - A list of animals currently inside
    """

    def __init__(self, size, environment_type, clean_level, animal_type):
        self.__size = size
        self.__environment_type = environment_type
        self.__clean_level = clean_level
        self.__animal_type = animal_type
        self.__animal = []

    # Add animal

    def add_animal(self, animal):
        """
        An animal is added to the enclosure if it matches the environment type
        """

        # Savannah = Mammals
        if self.environment_type == environment.Type.Savannah:
            if isinstance(animal, mammals.Mammal):
                self.__animal.append(animal)
                print(f"{animal} added to {environment.Type.Savannah.name} enclosure")

            else:
                print(f"{animal} cannot be added to {environment.Type.Savannah.name} enclosure, only mammals")

        # Wetlands = Reptiles
        elif self.environment_type == environment.Type.Wetlands:
            if isinstance(animal, reptiles.Reptile):
                self.__animal.append(animal)
                print(f"{animal} added to {environment.Type.Wetlands.name} enclosure")
            else:
                print(f"{animal} cannot be added to {environment.Type.Wetlands.name} enclosure, only reptiles")

        # Rainforest = Birds
        elif self.environment_type == environment.Type.Rainforest:
            if isinstance(animal, birds.Bird):
                self.__animal.append(animal)
                print(f"{animal} added to {environment.Type.Rainforest.name} enclosure")
            else:
                print(f"{animal} cannot be added to {environment.Type.Wetlands.name} enclosure, only birds")

    # status report
    def status(self):
        """
        Print the status of every animal in the enclosure.
        Includes:
            - Animal name
            - Environment type
            - Cleanliness level
        """

        for animal in self.__animal:
            print(f"{animal} added to {self.environment_type.name} enclosure")
            print(f"enclosure is {self.clean_level.name}")

    # Clean enclosure
    def clean_enclosure(self):
        """
        Set the enclosure cleanliness to 'Clean'.
        """

        self.__clean_level = environment.Clean_level.Clean

    def __str__(self):
        """
            Return a formatted description of the enclosure.
        """
        return (
            f"ENCLOSURE\n"
            f"Size: {self.size.name}\n"
            f"Environment: {self.environment_type.name}\n"
            f"Clean level: {self.clean_level.name}\n"
            f"Animal type: {self.animal_type.__name__}\n"
        )

    # Getter Methods (Encapsulation)
    def get_size(self):
        return self.__size

    def get_environment_type(self):
        return self.__environment_type

    def get_clean_level(self):
        return self.__clean_level

    def get_animal_type(self):
        return self.__animal_type

    def get_animal(self):
        return self.__animal

    # Properties to Private Attributes
    size = property(get_size)
    environment_type = property(get_environment_type)
    clean_level = property(get_clean_level)
    animal_type = property(get_animal_type)






