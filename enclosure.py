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
        if isinstance(animal, self.animal_type):
            if self.environment_type == environment.Type.Savannah:
                if self.animal_type == mammals.Mammal:
                    self.__animal.append(animal)
                    print("animal is mammal")

            elif self.environment_type == environment.Type.Wetlands:
                if self.animal_type == reptiles.Reptile:
                    self.__animal.append(animal)
                    print("animal is reptile")

            elif self.environment_type == environment.Type.Rainforest:
                if self.animal_type == birds.Bird:
                    self.__animal.append(animal)
                    print("animal is bird")



    def enclosure_type(self, enclosure):
        pass

    def status(self):
        for animal in self.__animal:
            print(animal)

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






