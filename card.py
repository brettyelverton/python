from functools imort total_ordering

@total_ordering
class Card(object):
	
	def	__init__(self, rank, suit, order=None):
		"""
		Create a card object with a string for the rank and suit.
		"""
		self._rank = rank
		self._suit = suit
		self._order = order
	
	def __repr__(self):
		return "Card({},".format(self._rank, self._suit) 
	
	def __str__(self):
		return "{}{}".format(self._rank, self._suit)
	
	def rank(self):
		return self._rank
	
	def __eq__(self, other):
		return self._rank == other.rank

	def __lt__(self, other):
		return self._order.find(self._rank) < self._order.find(other.rank())
