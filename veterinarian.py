from staff import Staff

class Veterinarian(Staff):
    def __init__(self, role, first_name, last_name, email):
        super().__init__(role, first_name, last_name, email)
        self.__assigned_animal = []
        self.__responsibilities = []

    def responsibility(self):
        print("Responsible for animal health checks")

    def add_animal(self, animal):
        self.__assigned_animal.append(animal)

    def task(self):
        for animal in self.__assigned_animal:
            pass



