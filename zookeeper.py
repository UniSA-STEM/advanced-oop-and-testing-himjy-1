import animal
from staff import Staff
from zoo import Zoo


class Zookeeper(Staff):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)

        # assign zookeeper species
        self.__responsibilities = ["mammal", "reptile", "birds"]

    def responsibility(self):
        for species in self.__responsibilities:
            if species == "mammal":
                print(f"Responsible for mammals")
            elif species == "reptile":
                print("Responsible for reptiles")
            elif species == "birds":
                print("Responsible for birds")

    def task(self):
        for animal in self.__animals:
            if animal.hunger:  # True means the animal is hungry
                print(f"{animal} is hungry. Feeding now...")
                animal.hunger = False # feed = sets hunger to False
            else:
                print(f"{animal} is not hungry.")

    def get_responsibilities(self):
        return self.__responsibilities

    zookeeper_reponsiblity = property(get_responsibilities)

