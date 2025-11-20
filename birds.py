from animal import Animal

class Bird(Animal):
    def __init__(self, name, species, age, diet):
        super().__init__(name, species, age, diet)

    def sound(self):
        print("bird sound")

    def eat(self):
        print("bird eat")

    def sleep(self):
        print("bird sleep")

