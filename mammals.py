from animal import Animal

class Mammal(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def sound(self):
        print("Mammal sound")

    def eat(self):
        print("Mammal eat")

    def sleep(self):
        print("Mammal sleep")

        