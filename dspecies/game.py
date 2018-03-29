#!/usr/bin/env python

import os
import random


class Game(object):
	"""Contains all the game players, elements, etc.
	"""
	def __init__(self):
		super(Game, self).__init__()

	def setup(self, num_players):
		self.players = []
		for x in range(num_players):
			p = Player(self.getPlayerName(x + 1))
			self.players.append(p)

	def getPlayerName(self, player_num):
		return input("Name for Player " + str(player_num + ":\t"))

	def run():
		pass
		
class Player(object):
	"""Corresponds a player to their hand, name, and score
	"""
	# Constants
	HAND_SIZE_LIMIT = 10

	def __init__(self, name):
		super(Player, self).__init__()
		self.name = name
		self.hand = Hand()
		
	def __str__(self):
		return self.name
		