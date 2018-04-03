#!/usr/bin/env python

"""board.py

Contains classes of various game components (e.g. board, tiles, pawns)
"""
import sys
sys.path.append("../")

import actions
from cat_enums import AnimalClass, TileBiome, Element
import d_const
import game
import random

class Board(object):
	"""Object containing all board state objects such as tiles and pawns
	"""
	def __init__(self):
		super(Board, self).__init__()
		self.map = HexGrid()
		self.tundra_tiles_stack = []
		self.biome_tiles_stack = [None,None,None]

	def setup(self, players):
		
		# add tundra tiles
		for x in range(d_const.NUM_TUNDRA_TILES):
			self.tundra_tiles_stack.append(TundraTile())

		# add biome stack
		b_stack = []
		for x in range(d_const.NUM_SEA_TILES):
			b_stack.append(BiomeTile(TileBiome.SEA))
		for x in range(d_const.NUM_WETLAND_TILES):
			b_stack.append(BiomeTile(TileBiome.WETLAND))
		for x in range(d_const.NUM_SAVANNAH_TILES):
			b_stack.append(BiomeTile(TileBiome.SAVANNAH))
		for x in range(d_const.NUM_DESERT_TILES):
			b_stack.append(BiomeTile(TileBiome.DESERT))
		for x in range(d_const.NUM_MOUNTAIN_TILES):
			b_stack.append(BiomeTile(TileBiome.MOUNTAIN))
		for x in range(d_const.NUM_FOREST_TILES):
			b_stack.append(BiomeTile(TileBiome.FOREST))
		for x in range(d_const.NUM_JUNGLE_TILES):
			b_stack.append(BiomeTile(TileBiome.JUNGLE))

		# shuffle and stack in groups of 8
		random.shuffle(b_stack)
		self.biome_tiles_stack[0] = b_stack[:8]
		self.biome_tiles_stack[1] = b_stack[8:16]
		self.biome_tiles_stack[2] = b_stack[16:]

		# initialize map with starting tiles
		self.map.add_tile(0,0,0,BiomeTile(TileBiome.SEA))
		self.map.add_tile(1,0,-1,BiomeTile(TileBiome.WETLAND))
		self.map.add_tile(1,-1,0,BiomeTile(TileBiome.SAVANNAH))
		self.map.add_tile(0,-1,1,BiomeTile(TileBiome.DESERT))
		self.map.add_tile(-1,0,1,BiomeTile(TileBiome.MOUNTAIN))
		self.map.add_tile(-1,1,0,BiomeTile(TileBiome.FOREST))
		self.map.add_tile(0,1,-1,BiomeTile(TileBiome.JUNGLE))

		self.map.add_tundra(0,0,0)

class HexGrid(object):
	"""HexGrid is the map of the Earth on the game board
	"""
	def __init__(self):
		super(HexGrid, self).__init__()

		# set hex coordinate bounds
		self.x_lo = -3
		self.x_hi = 3
		self.y_lo = -3
		self.y_hi = 3
		self.z_lo = -3
		self.z_hi = 3

		# fill grid will NIL tiles
		self.grid = []

		for x in range(abs(self.x_lo) + abs(self.x_hi) + 1):
			self.grid.append([])
			for y in range(abs(self.y_lo) + abs(self.y_hi) + 1):
				self.grid[x].append([])
				for z in range(abs(self.z_lo) + abs(self.z_hi) + 1):
					self.grid[x][y].append(0)
					self.grid[x][y][z] = BiomeTile(TileBiome.NIL)

	def get_tile(self, x, y, z):
		x_mid = round(len(self.grid)/2)
		y_mid = round(len(self.grid[0])/2)
		z_mid = round(len(self.grid[0][0])/2)
		return self.grid[x_mid + x][y_mid + y][z_mid + z]

	def add_tile(self, x, y, z, new_tile):
		x_mid = round(len(self.grid)/2)
		y_mid = round(len(self.grid[0])/2)
		z_mid = round(len(self.grid[0][0])/2)

		if self.grid[x_mid + x][y_mid + y][z_mid + z].type == TileBiome.NIL:
			self.grid[x_mid + x][y_mid + y][z_mid + z] = new_tile

		else:
			raise(ValueError("A tile already exists here!"))

	def add_tundra(self, x, y, z):
		x_mid = round(len(self.grid)/2)
		y_mid = round(len(self.grid[0])/2)
		z_mid = round(len(self.grid[0][0])/2)

		if self.grid[x_mid + x][y_mid + y][z_mid + z].type != TileBiome.NIL \
			or self.grid[x_mid + x][y_mid + y][z_mid + z].tundra != True:
			self.grid[x_mid + x][y_mid + y][z_mid + z].tundra = True

		elif self.grid[x_mid + x][y_mid + y][z_mid + z].type == TileBiome.NIL:
			raise(ValueError("Cannot place tundra tile on empty space."))

		else:
			raise(ValueError("A tundra tile already exists here."))

class ActionDisplay(object):
	"""docstring for ActionDisplay"""
	def __init__(self, arg):
		super(ActionDisplay, self).__init__()
		self.arg = arg

class ActionSpace(object):
	"""docstring for ActionSpace"""
	def __init__(self, arg):
		super(ActionSpace, self).__init__()
		self.arg = arg
						
class ADElementBox(object):
	"""docstring for ADElementBox"""
	def __init__(self, arg):
		super(ADElementBox, self).__init__()
		self.arg = arg

class ADAPCircle(object):
	"""docstring for ADAPCircle"""
	def __init__(self, arg):
		super(ADAPCircle, self).__init__()
		self.arg = arg
		
class ADElementDropdown(object):
	"""docstring for ADElementDropdown"""
	def __init__(self, arg):
		super(ADElementDropdown, self).__init__()
		self.arg = arg
		
class Tile(object):
	"""docstring for Tile"""
	def __init__(self):
		super(Tile, self).__init__()

class BiomeTile(Tile):
	"""tile making up the Earth on the game board"""
	def __init__(self, b_type):
		super(BiomeTile, self).__init__()
		self.type = b_type
		self.tundra = False
		
class TundraTile(Tile):
	"""Tundra tiles to be placed on top of other game tiles through glaciation
	"""
	def __init__(self):
		super(TundraTile, self).__init__()
		self.type = TileBiome.TUNDRA

class ACObject(object):
	"""docstring for ACObject"""
	def __init__(self, arg):
		super(ACObject, self).__init__()
		self.arg = arg
		
class ActionPawn(ACObject):
	"""docstring for ActionPawn"""
	def __init__(self, arg):
		super(ActionPawn, self).__init__()
		self.arg = arg
		
class SpeciesCube(ACObject):
	"""docstring for SpeciesCube"""
	def __init__(self, arg):
		super(SpeciesCube, self).__init__()
		self.arg = arg
		
class AnimalDisplay(ACObject):
	"""docstring for AnimalDisplay"""
	def __init__(self, arg):
		super(AnimalDisplay, self).__init__()
		self.arg = arg
		
class InitiativeMarker(ACObject):
	"""docstring for InitiativeMarker"""
	def __init__(self, arg):
		super(InitiativeMarker, self).__init__()
		self.arg = arg
		
class DCard(object):
	"""docstring for DCard"""
	def __init__(self, arg):
		super(DCard, self).__init__()
		self.arg = arg

class DCardDeck(object):
	"""docstring for DCardDeck"""
	def __init__(self, arg):
		super(DCardDeck, self).__init__()
		self.arg = arg
		
class GElement(object):
	"""Element object encapsulating an instance of one of the elements
	listed in the Element enumeration
	"""
	def __init__(self, element_type):
		super(GElement, self).__init__()
		self.element_type = element_type
		
class GElementBag(object):
	"""docstring for ElementBag"""
	def __init__(self, arg):
		super(GElementBag, self).__init__()
		self.arg = arg