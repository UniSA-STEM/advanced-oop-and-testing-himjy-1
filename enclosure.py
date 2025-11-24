'''
File: filename.py
Description: enclosure file.
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
    def __init__(self, size, environment_type, clean_level, animal_type):
        self.__size = size
        self.__environment_type = environment_type
        self.__clean_level = clean_level
        self.__animal_type = animal_type
        self.__animal = []

    def add_animal(self, animal):
        if self.environment_type == environment.Type.Savannah:
            if isinstance(animal, mammals.Mammal):
                self.__animal.append(animal)
                print(f"{animal} added to {environment.Type.Savannah.name} enclosure")

            else:
                print(f"{animal} cannot be added to {environment.Type.Savannah.name} enclosure, only mammals")

        elif self.environment_type == environment.Type.Wetlands:
            if isinstance(animal, reptiles.Reptile):
                self.__animal.append(animal)
                print(f"{animal} added to {environment.Type.Wetlands.name} enclosure")
            else:
                print(f"{animal} cannot be added to {environment.Type.Wetlands.name} enclosure, only reptiles")

        elif self.environment_type == environment.Type.Rainforest:
            if isinstance(animal, birds.Bird):
                self.__animal.append(animal)
                print(f"{animal} added to {environment.Type.Rainforest.name} enclosure")
            else:
                print(f"{animal} cannot be added to {environment.Type.Wetlands.name} enclosure, only birds")

    def status(self):
        for animal in self.__animal:
            print(f"{animal} added to {self.environment_type.name} enclosure")
            print(f"enclosure is {self.clean_level.name}")

    def clean_enclosure(self):
        self.__clean_level = environment.Clean_level.Clean

    def __str__(self):
        return (
            f"ENCLOSURE\n"
            f"Size: {self.size.name}\n"
            f"Environment: {self.environment_type.name}\n"
            f"Clean level: {self.clean_level.name}\n"
            f"Animal type: {self.animal_type.__name__}\n"
        )

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

    size = property(get_size)
    environment_type = property(get_environment_type)
    clean_level = property(get_clean_level)
    animal_type = property(get_animal_type)






