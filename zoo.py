from animal import Animal


class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        isinstance(animal, Animal)
        if animal not in self.__animals:
            self.__animals.append(animal)
            print(f"{animal} added")

    def remove_animal(self, animal):
        isinstance(animal, Animal)
        if animal in self.__animals:
            self.__animals.remove(animal)
            print(f"{animal} removed")


    def add_enclosure(self):
        pass

    def remove_enclosure(self):
        pass

    def add_staff(self):
        pass

    def remove_staff(self):
        pass

    def assign_animal(self):
        pass

    def daily_routine(self):
        pass

    def generate_report(self):
        pass

