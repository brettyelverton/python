from deck import *
from hand import *

deck = Deck()
deck.shuffle()

p1_hand = Hand()
p2_hand = Hand()

while len(deck) > 0:
	p1_hand.insert(deck.deal())
	p2_hand.insert(deck.deal())

round_number = 0
while len(p1_hand) != 0 and len(p2_hand) != 0:
	round_number += 1
	
	p1_played = Hand()
	p1_played.insert(p1_hand.deal())
	p2_played = Hand()
	p2_played.insert(p2_hand.deal())

	print("Round {}: ".format(round_number))
	print("Player 1: {}".format(p1_played))
	print("Player 2: {}".format(p2_played))
