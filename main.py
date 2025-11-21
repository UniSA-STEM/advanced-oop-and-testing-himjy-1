'''
File: main.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''
import enclosure
from animal import Animal
from zoo import Zoo
from mammals import Mammal
from birds import Bird
from reptiles import Reptile
from enclosure import Enclosure

zoo = Zoo()
zoo.add_animal('tiger')
zoo.remove_animal('tiger')

# Create animals
mammal1 = Mammal("Lion", "Panthera leo", 5, "Meat")
bird1 = Bird("Parrot", "Macaw", 2, "Seeds")
reptile1 = Reptile("Snake", "Python", 4, "Rodents")

# add animal to enclosure
mammal_enclosure = Enclosure('small', 'wetlands', 'clean', 'mammal')
mammal_enclosure.add_animal(mammal1)
mammal_enclosure.status()

#zookeeper
testing = zookeeper()