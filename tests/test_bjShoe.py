# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from bjShoe import Shoe
from card import Card
import pytest

def test_cardCounts():
	"""
	Check correct card counts when creating a shoe
	"""
	
	# Up to eight decks
	for x in range(1,9):
		s = Shoe(x)
		assert len(s.getCards()) == 52*x

def test_cardDistribution():
	"""
	Ensure we're getting the right number of card types (4 of each card) per deck
	"""
	
	# Up to eight decks
	for numDecks in range(1,9):
		# For each card name
		for name in Card.enumName.keys():
			# For each card suit
			for suit in Card.enumSuit:
				# Create the shoe
				s = Shoe(numDecks)
				s.shuffle()
				# count the number of times this specific card is found in the shoe
				c = len([myCard for myCard in s.getCards() if myCard.getName() == name and myCard.getSuit() == suit])
				# it should be equal to the number of decks in the shoe because there is only one of each card per deck
				assert c == numDecks

def test_cardDeal():
	"""
	Testing that our number of cards goes down by one when dealing a card
	"""
	
	s = Shoe(6)
	numCards = len(s.getCards())
	s.dealCard()
	numCardsAfter = len(s.getCards())
	assert numCardsAfter == numCards - 1

def test_dealSpecificCard():
	"""
	Testing that dealing a specific card really only deals that specific card
	"""
	
	# Up to eight decks
	for numDecks in range(1,9):
		# For each card name
		for name in Card.enumName.keys():
			# For each card suit
			for suit in Card.enumSuit:
				# Create the shoe
				s = Shoe(numDecks)
				s.shuffle()
				# Remove this card from the shoe
				s.dealSpecificCard(name,suit)
				# count the number of times this specific card is found in the shoe
				c = len([myCard for myCard in s.getCards() if myCard.getName() == name and myCard.getSuit() == suit])
				# it should be equal to the number of decks in the shoe minus the one we just dealt
				assert c == numDecks - 1


def test_dealSpecificCardException():
	"""
	Ensure that we're raising an exception when we can't deal a specific card.
	"""
	
	s = Shoe(6)
	s.shuffle()
	
	for x in range(0,6):
		s.dealSpecificCard("9","Spade")
	
	# This should be an exception
	with pytest.raises(Exception):
		s.dealSpecificCard("9","Spade")

def test_printShoe():
	"""
	Just testing that printShoe doesn't error out. Not sure how to test UI output.
	"""
	
	s = Shoe(6)
	s.shuffle()
	# Implicitly asserting that there is no exception
	s.printShoe()
