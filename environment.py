'''
File: environment.py
Description: main file.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from enum import Enum

class Type(Enum):
    Rainforest = 1
    Savannah = 2
    Wetlands = 3


class Size(Enum):
    Small = 1
    Medium = 2
    Large = 3

class Clean_level(Enum):
    Dirty = 1
    NeedsCleaning = 2
    Clean = 3