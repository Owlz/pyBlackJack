# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from deck import Deck

def test_deck52Cards():
	"""
	Checks if returned deck is a normal 52 card deck.
	"""
	myDeck = Deck()
	myDeck.shuffle()
	
	cards = myDeck.getCards()
	assert len(cards) == 52
	
