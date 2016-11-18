from card import *
import random


class Deck(object):
	
	def __init__(self):
		ranks = [str(a) for a in range(2,10)] + list('TJQKA')
		suits = 'DCHS'

		self._contents = [Card(rank, suit, ''.join(ranks)) for suit in suits for rank in ranks]

	def __repr__(self):
		return "Deck({})".format(self._contents)

	def __str__(self):
		return str([str(card) for card in self._contents])

	def deal(self):
		return self._contents.pop(0)

	def shuffle(self):
		random.shuffle(self._contents)

	def __len__(self):
		return len(self._contents)

##start here: create and display decks
