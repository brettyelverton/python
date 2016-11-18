from card import *


class Hand(object):
	
	def __init__(self, contents = None):
		self._contents = contents if contents else []

		# if contents is nont None:
		#	self._contents = contents
		# else:
		#	self._contents = []

	def __repr__(self):
		return "Hand({})".format(self._contents)

	def __str__(self):
		return str([str(card) for card in self._contents])

	def insert(self, card):
		self._contents.append(card)
		

	def deal(self):
		return self._contents.pop(0)

	def __len__(self):
		return len(self._contents)

	def contents(self):
		return self._contents.copy()

	def __add__(self, other):
		if type(other) is Card:
			return Hand(self._contents + [other])
		else:
			return Hand(self._contents + other.contents())

