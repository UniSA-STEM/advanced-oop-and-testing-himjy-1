'''
File: veterinarian.py
Description: Defines the Veterinarian subclass of Staff.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Veterinarian(Staff):
    """
    Veterinarians:
        - Perform medical checks on animals
        - Heal sick animals
        - Maintain health records
        - Are assigned specific animals to care for

    """
    def __init__(self, role, first_name, last_name, email):
        super().__init__(role, first_name, last_name, email)
        self.__assigned_animal = []
        self.__responsibilities = []

    # Required abstract method implementation
    def responsibility(self):
        print("Responsible for animal health checks")

    def task(self):
        for animal in self.__assigned_animal:
            if animal.health < 50:
                print(f"{animal} requires medical attention")
            else:
                print(f"{animal} is Healthy")

    # Animal Management
    def add_animal(self, animal):
        self.__assigned_animal.append(animal)

    # Healing Process
    def heal(self):
        for animal in self.__assigned_animal:
            if animal.health < 50:
                animal.heal(100)
                print(f"{animal} has received medical care and is fully restored")
            else:
                print(f"{animal} is healthy and does not require medical attention")



