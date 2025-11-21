from staff import Staff

class Veterinarian(Staff):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)

    def responsibility(self):
        pass

    def task(self):
        pass


