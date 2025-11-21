import animal
from staff import Staff
from zoo import Zoo


class Zookeeper(Staff):
    def __init__(self, first_name, last_name, email):
        super().__init__(first_name, last_name, email)
        self.__responsibilities = ["mammal", "reptile", "birds"]

    def responsibility(self):
        if self.zookeeper_reponsiblity[0]:
            print("reponsbile for birds")

        elif self.zookeeper_reponsiblity == "mammal":
            print("reponsbile for mammal")

        elif self.zookeeper_reponsiblity == "reptile":
            print("reponsbile for reptile")


    def task(self):
        pass

    def get_responsibilities(self):
        return self.__responsibilities

    zookeeper_reponsiblity = property(get_responsibilities)

