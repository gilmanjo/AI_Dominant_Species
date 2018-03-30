from enum import Enum


"""types.py

Contains enumerations for various categorical values used in Dominant Species.
For AI, these need to be one-hot encoded!
"""
class AnimalClass(Enum):
	INSECT = 1
	ARACHNID = 2
	AMPHIBIAN = 3
	BIRD = 4
	REPTILE = 5
	MAMMAL = 6
	NIL = 0

class TileBiome(Enum):
	MOUNTAIN = 1
	DESERT = 2
	FOREST = 3
	JUNGLE = 4
	SAVANNAH = 5
	WETLAND = 6
	SEA = 7
	NIL = 0

class Element(Enum):
	GRASS = 1
	GRUB = 2
	MEAT = 3
	SEED = 4
	SUN = 5
	WATER = 6
	NIL = 0