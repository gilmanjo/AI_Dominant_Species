#!/usr/bin/env python

import sys
sys.path.append("../dspecies")
import game
import unittest
from unittest.mock import patch


# Unit tests for running the Jump Drive game
class GameTests(unittest.TestCase):

	def setUp(self):
		self.game = game.Game()

	# Test that a two players exist after running a two player setup
	@patch("game.Game.getPlayerName")
	def testTwoPlayerSetup(self, getPlayerName):
		# Mock player names
		m = unittest.mock.Mock()
		m.side_effect = ["Jordan", "Robot"]
		getPlayerName.return_value = m
		self.game.setup(2)

		self.assertIsInstance(self.game.players[1], game.Player)
		self.assertIsInstance(self.game.players[0], game.Player)

	# Tests all cards are unique
	def testAllUniqueCards(self):
		d = game.Deck()
		ids = []
		for x in d.cards:
			for y in ids:
				self.assertNotEqual(x.card_id, y)
			ids.append(x.card_id)

	# Tests that drawn cards are removed from the deck
	def testDeckGetCard(self):
		d = game.Deck()
		card = d.drawCard()
		for x in d.cards:
			self.assertNotEqual(card.card_id, x.card_id)

def main():
	unittest.main()

if __name__ == "__main__":
	main()