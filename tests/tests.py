#!/usr/bin/env python

import sys
sys.path.append("../dspecies")
sys.path.append("../dspecies/components")

import actions
import board
from cat_enums import AnimalClass, TileBiome
import d_const
import game
import unittest
from unittest.mock import patch


# Unit tests for running the Dominant Species game logic
class GameTests(unittest.TestCase):

	def setUp(self):
		self.game = game.Game()

	# helper function to setup game for more intermediate testing
	def _start_game(self, num_players):
		new_game = game.Game()
		new_game.setup(num_players, player_names=["Alpha", "Bravo", "Charlie",
			"Delta", "Echo", "Foxtrot"], player_acs=["MAMMAL", "REPTILE",
			"BIRD", "AMPHIBIAN", "ARACHNID", "INSECT"])
		self.game = new_game

	# Test that a two players exist after running a two player setup
	@patch("game.Game.set_player_name")
	def testTwoPlayerSetup(self, set_player_name):

		# Mock player names
		set_player_name.side_effect = ["Jordan", "Robot"]
		self.game.setup(2, player_acs=["BIRD", "BIRD"])

		self.assertIsInstance(self.game.players[1], game.Player)
		self.assertIsInstance(self.game.players[0], game.Player)

	@patch("game.Game.set_player_name")
	def testThreePlayerSetup(self, set_player_name):
		set_player_name.side_effect = ["Jordan", "Robot", "Cyborg"]
		self.game.setup(3, player_acs=["BIRD", "BIRD", "BIRD"])

		self.assertIsInstance(self.game.players[2], game.Player)
		self.assertIsInstance(self.game.players[1], game.Player)
		self.assertIsInstance(self.game.players[0], game.Player)

	@patch("game.Game.set_player_name")
	def testSixPlayerSetup(self, set_player_name):
		set_player_name.side_effect = ["Jordan", "Robot", "Cyborg", "BOT",
			"HAL9000", "Eric"]
		self.game.setup(6, player_acs=["BIRD", "BIRD", "BIRD", "BIRD", "BIRD",
			"BIRD"])

		self.assertIsInstance(self.game.players[5], game.Player)
		self.assertIsInstance(self.game.players[4], game.Player)
		self.assertIsInstance(self.game.players[3], game.Player)
		self.assertIsInstance(self.game.players[2], game.Player)
		self.assertIsInstance(self.game.players[1], game.Player)
		self.assertIsInstance(self.game.players[0], game.Player)

	@patch("game.Game.set_player_ac")
	@patch("game.Game.set_player_name")
	def testTwoPlayerSetupAnimalClasses(self, set_player_name, set_player_ac):
		set_player_name.side_effect = ["Jordan", "Robot"]
		set_player_ac.side_effect = ["Reptile", "Arachnid"]
		self.game.setup(2)

		self.assertEqual(self.game.players[1].ac, AnimalClass.ARACHNID)
		self.assertEqual(self.game.players[0].ac, AnimalClass.REPTILE)

	@patch("game.Game.set_player_ac")
	@patch("game.Game.set_player_name")
	def testThreePlayerSetupAnimalClasses(self, set_player_name, 
		set_player_ac):

		set_player_name.side_effect = ["Jordan", "Robot", "Cyborg"]
		set_player_ac.side_effect = ["Reptile", "Arachnid", "Amphibian"]
		self.game.setup(3)

		self.assertEqual(self.game.players[2].ac, AnimalClass.AMPHIBIAN)
		self.assertEqual(self.game.players[1].ac, AnimalClass.ARACHNID)
		self.assertEqual(self.game.players[0].ac, AnimalClass.REPTILE)

	@patch("game.Game.set_player_ac")
	@patch("game.Game.set_player_name")
	def testSixPlayerSetupAnimalClasses(self, set_player_name, set_player_ac):
		set_player_name.side_effect = ["Jordan", "Robot", "Cyborg", "BOT",
			"HAL9000","Eric"]
		set_player_ac.side_effect = ["Reptile", "Arachnid", "Amphibian",
			"Mammal", "Bird", "Insect"]
		self.game.setup(6)

		self.assertEqual(self.game.players[5].ac, AnimalClass.INSECT)
		self.assertEqual(self.game.players[4].ac, AnimalClass.BIRD)
		self.assertEqual(self.game.players[3].ac, AnimalClass.MAMMAL)
		self.assertEqual(self.game.players[2].ac, AnimalClass.AMPHIBIAN)
		self.assertEqual(self.game.players[1].ac, AnimalClass.ARACHNID)
		self.assertEqual(self.game.players[0].ac, AnimalClass.REPTILE)

	def testGameBoardInitialization(self):
		self._start_game(3)

		# players start at 0 VP
		self.assertEqual(self.game.players[2].vps, 0)
		self.assertEqual(self.game.players[1].vps, 0)
		self.assertEqual(self.game.players[0].vps, 0)

		# board exists
		self.assertIsInstance(self.game.board, board.Board)

	def testGameBoardInitStacks(self):
		self._start_game(3)

		# biome and tundra tiles initialized
		self.assertEqual(len(self.game.board.tundra_tiles_stack), 
			d_const.NUM_TUNDRA_TILES)
		for tile in self.game.board.tundra_tiles_stack:
			self.assertIsInstance(tile, board.TundraTile)

		self.assertEqual(len(self.game.board.biome_tiles_stack[0]),
			d_const.BIOME_TILE_STACK_SIZE)
		self.assertEqual(len(self.game.board.biome_tiles_stack[1]),
			d_const.BIOME_TILE_STACK_SIZE)
		self.assertEqual(len(self.game.board.biome_tiles_stack[2]),
			d_const.BIOME_TILE_STACK_SIZE)

		for stack in self.game.board.biome_tiles_stack:
			for tile in stack:
				self.assertIsInstance(tile, board.BiomeTile)

	def testGameBoardInitTilePlacement(self):
		self._start_game(3)

		# correct tiles in starting grid positions
		self.assertEqual(self.game.board.map.get_tile(0,0,0).type,
			TileBiome.SEA)
		self.assertEqual(self.game.board.map.get_tile(1,0,-1).type,
			TileBiome.WETLAND)
		self.assertEqual(self.game.board.map.get_tile(1,-1,0).type,
			TileBiome.SAVANNAH)
		self.assertEqual(self.game.board.map.get_tile(0,-1,1).type,
			TileBiome.DESERT)
		self.assertEqual(self.game.board.map.get_tile(-1,0,1).type,
			TileBiome.MOUNTAIN)
		self.assertEqual(self.game.board.map.get_tile(-1,1,0).type,
			TileBiome.FOREST)
		self.assertEqual(self.game.board.map.get_tile(0,1,-1).type,
			TileBiome.JUNGLE)

	def testGameBoardInitTundraPlacement(self):
		self._start_game(3)

		# correct tundra placement
		self.assertEqual(self.game.board.map.get_tile(0,0,0).tundra, True)
		self.assertEqual(self.game.board.map.get_tile(1,0,-1).tundra, False)
		self.assertEqual(self.game.board.map.get_tile(1,-1,0).tundra, False)
		self.assertEqual(self.game.board.map.get_tile(0,-1,1).tundra, False)
		self.assertEqual(self.game.board.map.get_tile(-1,0,1).tundra, False)
		self.assertEqual(self.game.board.map.get_tile(-1,1,0).tundra, False)
		self.assertEqual(self.game.board.map.get_tile(0,1,-1).tundra, False)

	def testGameBoardInitSpeciesPlacement(self):
		pass

	def testGameBoardInitInitiativeThree(self):
		pass

	def testGameBoardInitInitiativeSix(self):
		pass

	def testGameBoardInitElementBoxes(self):
		pass

	def testGameBoardInitElementDropdown(self):
		pass

	def testGameBoardInitAPSpaces(self):
		pass

	def testGameBoardInitDCards(self):
		pass


# Unit test for implementation of AI methods for game
class AITests(unittest.TestCase):
	pass

def main():
	unittest.main()

if __name__ == "__main__":
	main()