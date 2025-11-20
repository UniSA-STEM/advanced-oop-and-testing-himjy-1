from enum import Enum

class Environment_type(Enum):
    Aquarium = 1
    Savannah = 2
    Rainforest = 3
    Wetlands = 4

class Enclosure_size(Enum):
    Small = 1
    Medium = 2
    Large = 3

class Enclosure_clean_level(Enum):
    Dirty = 1
    NeedsCleaning = 2
    Clean = 3