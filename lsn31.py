class Card(object):
	
	def	__init__(self, rank, suit):
		"""
		Create a card object with a string for the rank and suit.
		"""
		self._rank = rank
		self._suit = suit
	def __repr__(self):
		return "Card({},".format(self._rank, self._suit) 
	def __str__(self):
		return "{}{}".format(self._rank, self._suit)
		
