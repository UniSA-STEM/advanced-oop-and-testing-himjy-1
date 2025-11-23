import environment
from staff import Staff
from environment import Clean_level


class Zookeeper(Staff):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.__assigned_animal = []
        self.__assigned_enclosure = []

        # assign zookeeper species
        self.__responsibilities = ["mammal", "reptile", "birds"]

    def add_animal(self, animal):
        if animal not in self.__assigned_animal:
            self.__assigned_animal.append(animal)

    def add_enclosure(self, enclosure):
        if enclosure not in self.__assigned_enclosure:
            self.__assigned_enclosure.append(enclosure)

    def responsibility(self):
        for species in self.__responsibilities:
            if species == "mammal":
                print(f"Responsible for mammals")
            elif species == "reptile":
                print("Responsible for reptiles")
            elif species == "birds":
                print("Responsible for birds")

    def task(self):
        for animal in self.__assigned_animal:
            if animal.hunger:  # True means the animal is hungry
                print(f"{animal} is hungry. Feeding now...")
                animal.feed()  # feed = sets hunger to False
            else:
                print(f"{animal} is not hungry.")

    def clean(self):
        for enclosure in self.__assigned_enclosure:
            if enclosure.clean_level == Clean_level.Dirty or enclosure.clean_level == Clean_level.NeedsCleaning:
                print("needs cleaning")
                enclosure.clean_enclosure()
            else:
                print("clean")

    def get_responsibilities(self):
        return self.__responsibilities

    def get_animal(self):
        return self.__assigned_animal

    assigned_animals = property(get_animal)
    zookeeper_responsibility = property(get_responsibilities)

