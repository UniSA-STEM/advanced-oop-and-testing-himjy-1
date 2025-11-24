import environment
from staff import Staff
from environment import Clean_level
from environment import Type

class Zookeeper(Staff):
    def __init__(self, role, first_name, last_name, email):
        super().__init__(role, first_name, last_name, email)
        self.__assigned_animal = []
        self.__assigned_enclosure = []
        self.__responsibilities = ["mammal", "reptile", "birds"]

    def add_animal(self, animal):
        if animal not in self.__assigned_animal:
            self.__assigned_animal.append(animal)
            print(f"{animal} assigned to Zookeeper")

    def add_enclosure(self, enclosure):
        if enclosure not in self.__assigned_enclosure:
            self.__assigned_enclosure.append(enclosure)
            print(f"enclosure assigned to Zookeeper")

    def responsibility(self):
        print("Zookeeper is responsible for feeding the animals and cleaning the enclosure")

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
                print("this enclosure needs cleaning")
                enclosure.clean_enclosure()
                print("enclosure is cleaned")
            else:
                print("enclosure is not dirty")

    def get_responsibilities(self):
        return self.__responsibilities

    def get_animal(self):
        return self.__assigned_animal

    assigned_animals = property(get_animal)
    zookeeper_responsibility = property(get_responsibilities)

