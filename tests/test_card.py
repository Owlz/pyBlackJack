# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from card import Card

def test_basicCardCreation():
	"""
	Create some basic cards and make sure they come out ok.
	"""
	c = Card("A","Diamond")
	assert c.getName() == "A"
	assert c.getValue() == [1,11]
	assert c.getSuit() == "Diamond"

def test_invalidCardCreation():
	"""
	Create cards that shouldn't exist and make sure they raise an error.
	"""
	
	# No initial value
	with pytest.raises(Exception):
		c = Card(None,"Diamond")
	
	with pytest.raises(Exception):
		c = Card("A",None)
	
	# Invalid types
	with pytest.raises(Exception):
		c = Card("B","Diamond")
	
	with pytest.raises(Exception):
		c = Card("A","Something")	
