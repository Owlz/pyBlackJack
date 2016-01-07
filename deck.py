from card import *
from random import shuffle

class Deck:
	"""
	Define what a Deck is
	"""

	def __init__(self):
		"""
		Initialize the deck. No shuffling is done
		"""

		# Keeps track of what cards are in the deck
		self.cards = []

		for value in list(range(2,11)) + ["J","Q","K","A"]:
			for suit in ["Spade","Diamond","Heart","Club"]:
				self.cards.append(Card(str(value),suit))

	def getCards(self):
		"""
		Returns a list of cards in the deck as objects
		"""
		# Return a copy of the cards, not the cards themselves
		return self.cards[:]

	def shuffle(self):
		"""
		Shuffles the current deck
		"""
		shuffle(self.cards)
