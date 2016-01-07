def ofType(item, type):
	return item.__class__.__name__ == type


class Player:
	"""
	This class defines a blackjack player. Each blackjack player can have one or more hands.
	"""

	def __init__(self, money, strategy):
		"""
		Initialize the player
		"""

		# How much money does this player have
		self.money = money

		# Import this person's strategy
		self.strategy = __import__(strategy).strategy

		# Start up our hands spots
		self.hands = []

	def addHand(self, hand):
		"""
		Add a given hand to the user's list
		"""

		# Make this really is a hand object
		assert ofType(hand, "Hand")

		self.hands.append(hand)

	def getHand(self, index=0):
		"""
		Returns a pointer to the hand at index
		"""
		return self.hands[0]
