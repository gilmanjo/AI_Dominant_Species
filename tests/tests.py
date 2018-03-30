#!/usr/bin/env python

import sys
sys.path.append("../dspecies")
sys.path.append("../dspecies/components")

from cat_enums import AnimalClass
import game
import unittest
from unittest.mock import patch


# Unit tests for running the Dominant Species game logic
class GameTests(unittest.TestCase):

	def setUp(self):
		self.game = game.Game()

	# helper function to setup game for more intermediate testing
	def _start_game(self, num_players):
		game = game.Game()
		game.setup(num_players, player_names=["Alpha", "Bravo", "Charlie",
			"Delta", "Echo", "Foxtrot"], player_acs=["MAMMAL", "REPTILE",
			"BIRD", "AMPHIBIAN", "ARACHNID", "INSECT"])
		return game

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

# Unit test for implementation of AI methods for game
class AITests(unittest.TestCase):
	pass

def main():
	unittest.main()

if __name__ == "__main__":
	main()