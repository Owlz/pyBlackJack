# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

from bjHand import Hand
from card import Card

def test_initHand():
	"""
	Excersize initializing a Hand object
	"""
	
	# Check #1 -- Make sure Hand object works
	h = Hand()
	
	# Dummy cards for testing
	c1 = Card("A","Heart")
	c2 = Card("9","Spade")
	
	# Create Hand with 1 card
	h = Hand(c1)
	
	# Create Hand with 2 cards
	h = Hand(c1,c2)
	
	# Create Hand with bad 1st card
	with pytest.raises(AssertionError):
		h = Hand("test")
	
	# Create Hand with bad 2nd card
	with pytest.raises(AssertionError):
		h = Hand(c1,"test")

def test_addCard():
	"""
	Test adding a card to a hand
	"""
	
	# Create the hand
	h = Hand()
	
	# Create a card
	c = Card("Q","Diamond")
	
	# Add the card
	h.addCard(c)
	
	# Check that it was added
	assert len(h.getCards()) == 1
	
	# Try to add a card that isn't a card object
	with pytest.raises(AssertionError):
		h.addCard("Hello")
	
def test_getCards():
	"""
	Test out getting the list of cards.
	"""
	
	# Create the hand
	h = Hand()
	
	# Create the cards
	c1 = Card("K","Club")
	c2 = Card("J","Spade")
	
	# Add the card
	h.addCard(c1)
	h.addCard(c2)
	
	# Get the card
	cards = h.getCards()
	
	# Assert that we got them back
	assert c1 in cards
	assert c2 in cards

def test_getValue():
	"""
	Ensure we're getting values the way we think we are
	"""
	
	# Create a hand
	h = Hand()
	
	# Add a card
	c1 = Card("A","Club")
	h.addCard(c1)
	
	# Check the hand values
	val = h.getValue()
	assert len(val) == 2
	assert val[0] == 1
	assert val[1] == 11
	
	# Add another card
	c2 = Card("Q","Club")
	h.addCard(c2)
	
	# Check hand value
	val = h.getValue()
	assert len(val) == 2
	assert val[0] == 11
	assert val[1] == 21
	
	# One more card
	c3 = Card("5","Spade")
	h.addCard(c3)
	
	# Check it
	val = h.getValue()
	assert len(val) == 1
	assert val[0] == 16

def test_printCards():
	"""
	Just print the cards in various ways
	"""
	
	c1 = Card("A","Spade")
	c2 = Card("Q","Club")
	
	h = Hand(c1,c2)
	
	h.printCards()
	h.pprint(isDealer=False)
	h.pprint(isDealer=True)

def test_isBlackJack():
	"""
	Test the isBlackJack function
	"""
	
	c1 = Card("A","Spade")
	c2 = Card("J","Diamond")
	
	h = Hand(c1,c2)
	
	assert h.isBlackJack()
	
	c3 = Card("6","Spade")
	h = Hand(c1,c3)
	
	assert not h.isBlackJack()

def test_isBusted():
	"""
	Test the isBusted function
	"""
	
	c1 = Card("5","Spade")
	c2 = Card("7","Diamond")
	
	h = Hand(c1,c2)
	
	assert not h.isBusted()
	
	c3 = Card("Q","Club")
	h.addCard(c3)
	
	assert h.isBusted()
