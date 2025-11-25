'''
File: main.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''
import environment
from veterinarian import Veterinarian
from zoo import Zoo
from mammals import Mammal
from birds import Bird
from reptiles import Reptile
from enclosure import Enclosure
from zookeeper import Zookeeper

# Create animals
mammal1 = Mammal("Lion", "Panthera leo", 5, "Meat")
bird1 = Bird("Parrot", "Macaw", 2, "Seeds")
reptile1 = Reptile("Snake", "Python", 4, "Rodents")

# Staff
zookeeper1 = Zookeeper('zookeeper','jamie', 'himmy', '@hotmail.com')
veterinarian1 = Veterinarian('veterinarian', 'james', 'him', '@gmail.com')


#Zoo
print("WELCOME TO THE ZOO\n")
zoo = Zoo()
zoo.add_animal('tiger')
zoo.remove_animal('tiger')
print(f"---------\n")

# animal sound
mammal1.sound()
bird1.sound()
print("\n")

# 1 — Mammal enclosure (Savannah)
enclosure1 = Enclosure(
    environment.Size.Small,
    environment.Type.Savannah,
    environment.Clean_level.Dirty,
    Mammal
)

# 2 — Bird enclosure (Rainforest)
enclosure2 = Enclosure(
    environment.Size.Medium,
    environment.Type.Rainforest,
    environment.Clean_level.NeedsCleaning,
    Bird
)

# 3 — Reptile enclosure (Wetlands)
enclosure3 = Enclosure(
    environment.Size.Large,
    environment.Type.Wetlands,
    environment.Clean_level.Clean,
    Reptile
)

enclosure1.add_animal(bird1)
enclosure2.add_animal(mammal1)
enclosure2.add_animal(bird1)
enclosure1.status()
print(enclosure1)


# add animal to enclosure

# zookeeper
print(f"\n---------")
print(zookeeper1)
zookeeper1.add_animal(mammal1)
zookeeper1.responsibility()
zookeeper1.task()
zookeeper1.task()

zookeeper1.add_enclosure(enclosure1)
zookeeper1.clean()

print(f"---------\n")

# veterinarian
print(veterinarian1)
veterinarian1.add_animal(mammal1)
veterinarian1.responsibility()
veterinarian1.task()
mammal1.sick(50)
veterinarian1.heal()
