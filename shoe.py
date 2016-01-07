from random import shuffle
from deck import *

class Shoe:
	"""
	Class describes a "shoe" (multiple decks)
	"""

	def __init__(self,nDecks):
		"""
		Initialize the shoe with n number of decks
		"""
		# Hold the non-discarded cards
		self.cards = []

		for x in range(0,nDecks):
			self.cards += Deck().getCards()

	def shuffle(self):
		"""
		Shuffle the shoe.
		"""
		shuffle(self.cards)

	def getCards(self):
		"""
		Return a list of card objects left in the deck
		"""
		return self.cards[:]

	def dealCard(self):
		"""
		Pops the top card off the deck. Simulates dealing of a card.
		"""
		return self.popCardIndex(0)

	def popCardIndex(self,i):
		"""
		Pops the given card.
		"""
		return self.cards.pop(i)

	def dealSpecificCard(self,name=None,suit=None):
		"""
		Deal a specific card (name, suit, or both).
		This is helpful for creating scenarios to test
		"""
		# This algorithm kinda sucks...

		cards = self.getCards()
		
		for i in range(0,len(cards)):
			# If this card matches our description
			if (cards[i].getSuit() == suit and cards[i].getName() == name) or (name == None and cards[i].getSuit() == suit) or (suit == None and cards[i].getName() == name):
				return self.popCardIndex(i)

		raise Exception("Couldn't pop specific card {0} of {1}".format(name,suit))

	def printShoe(self):
		"""
		Print out all the cards in the shoe
		"""

		for c in self.getCards():
			print "{0} of {1}".format(c.getName(), c.getSuit())

