'''
File: filename.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal
from zoo import Zoo
from mammals import Mammal
from birds import Bird
from reptiles import Reptile


zoo = Zoo()
zoo.add_animal('tiger')
zoo.remove_animal('tiger')

mammal1 = Mammal('Monkey', 'Mammal', '9', 'bananas')
mammal1.sound()

bird1 = Bird('Parrots', 'Cockatiel', '3', ' leafy greens')
bird1.eat()

reptile1 = Reptile('Snake', 'Python', '4', 'rodents')
reptile1.sleep()

