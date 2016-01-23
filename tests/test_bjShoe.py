# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from bjShoe import Shoe

def test_cardCounts():
	"""
	Check correct card counts when creating a shoe
	"""
	
	# Up to eight decks
	for x in range(1,9):
		s = Shoe(x)
		assert len(s.getCards()) == 52*x
