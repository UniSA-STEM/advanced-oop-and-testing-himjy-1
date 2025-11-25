'''
File: environment.py
Description: Defines environment, size, and cleanliness enums for zoo enclosures.
Author: Jamie Him
ID: 110375225
Username: himjy003
This is my own work as defined by the University's Academic Integrity Policy.
'''

from enum import Enum

class Type(Enum):
    """
    Represents the different environment types available in the zoo.

    These environment types determine which animals
    can be placed into an enclosure:

    """
    Rainforest = 1
    Savannah = 2
    Wetlands = 3

class Size(Enum):
    """
    Represents the size of an enclosure.

    These values describe physical dimensions or capacity:

    """

    Small = 1
    Medium = 2
    Large = 3

class Clean_level(Enum):
    """
     Represents how clean an enclosure currently is.

     This is used by zookeepers and other staff to determine
     whether an enclosure requires cleaning.

     """
    Dirty = 1
    NeedsCleaning = 2
    Clean = 3