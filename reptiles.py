    from animal import Animal

    class Reptile(Animal):
        def __init__(self, name, species, age, diet):
            super().__init__(name, species, age, diet)

        def sound(self):
            print("Reptile sound")

        def eat(self):
            print("Reptile eat")

        def sleep(self):
            print("Reptile sleep")