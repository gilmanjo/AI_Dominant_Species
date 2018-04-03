#!/usr/bin/env python

import sys
sys.path.append("../components")

import board
from cat_enums import AnimalClass
import d_const
import os
import random
import types


class Game(object):
	"""Contains all the game players, elements, etc.
	"""
	def __init__(self):
		super(Game, self).__init__()

	def setup(self, num_players, player_names=None, player_acs=None):
		
		# Get player information
		self.players = []
		self.init_players(num_players, player_names, player_acs)
		
		# TODO: Initialize game board
		self.board = board.Board()
		self.board.setup(self.players)

	def init_players(self, num_players, player_names, player_acs):

		for x in range(1, num_players + 1):	# 0 to player_num

			# default if not running in terminal
			if player_names is None:
				p = Player(self.set_player_name(x))
				
			else:
				p = Player(player_names[x - 1])

			# default if not running in terminal
			if player_acs is None:
				p.ac = AnimalClass[self.set_player_ac(x).upper()]

			else:
				p.ac = AnimalClass[player_acs[x - 1]]

			self.players.append(p)

	def set_player_name(self, player_num):
		return input("Name for Player " + str(player_num) + ":\t")

	def set_player_ac(self, player_num):
		return input("Animal Class for Player " + str(player_num) + ":\t")

	def run():
		pass
		
class Player(object):
	"""Matches a player to their animal class
	"""
	# Constants
	HAND_SIZE_LIMIT = 10

	def __init__(self, name, ac=AnimalClass.NIL):
		super(Player, self).__init__()
		self.name = name
		self.ac = ac
		self.vps = 0
		
	def __str__(self):
		return "{} - {}".format(self.name, self.ac)
		