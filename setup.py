#!/usr/bin/env python

from setuptool import setup

with open("README", "r") as f:
	long_description = f.read()

setup(
	name="dspecies",
	version=0.01,
	description="AI Application to the game 'Dominant Species'",
	author="Jordan Gilman",
	author_email="gilmanjo@oregonstate.edu"
)