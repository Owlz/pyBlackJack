def isCard(item):
	return item.__class__.__name__ == "Card"

class Hand:
	"""
	Defines a blackjack hand
	"""

	def __init__(self, card1 = None, card2 = None):
		"""
		Initialize the blackjack hand
		"""

		# What cards are in the hand
		self.cards = []

		# If we are giving initial cards, add them
		if card1 != None:
			# These should be cards
			assert isCard(card1)
			self.cards.append(card1)

		if card2 != None:
			assert isCard(card2)
			self.cards.append(card2)

		return

	def addCard(self, card):
		"""
		Add a card to the hand
		"""
		assert isCard(card)

		self.cards.append(card)

	def getCards(self):
		"""
		Return array of cards in the hand
		"""

		# Return a copy
		return self.cards[:]


	def getValue(self):
		"""
		Determine hand total value
		Returns as an array (i.e.: [5] or [7,17])
		"""

		total = [0]

		for card in self.getCards():
			temp = []
			for value in card.getValue():
				for t in total:
					temp.append(t + value)

			# Remove duplicates
			temp = sorted(list(set(temp)))

			# Remove entries greater than 21
			temp = [x for x in temp if x <= 21]
	
			total = temp

		return total

	def printCards(self):
		"""
		Prints out description of what cards are in the hand
		"""

		for card in self.getCards():
			print("{0} of {1}".format(card.getName(), card.getSuit()))

	def pprint(self,isDealer=False):
		"""
		Pretty print cards in ASCII art
		If it's the dealer's hand, hide the second card
		"""
		# Some code stolen from http://stackoverflow.com/questions/983699/initialise-a-list-to-a-specific-length-in-python
		
		# Suit lookup in unicode range
		suitLookup = {
			"Diamond": chr(0x2666),
			"Spade": chr(0x2660),
			"Heart": chr(0x2665),
			"Club": chr(0x2663)}
		# Initialize the lines
		lines = [""] * 9
		
		# Loop through all the hards in your hand
		for card in self.getCards():
			# If we're printing the dealer's hand, don't show the second card
			if isDealer == True and self.getCards().index(card) == 1:
				continue

			# Format the cards line by line so that they line up horizontally
			lines[0] += ('┌─────────┐ ')
			lines[1] += ('│{0:<5}    │ '.format(card.getName()))
			lines[2] += ('│         │ ')
			lines[3] += ('│         │ ')
			lines[4] += ('│    {}    │ '.format(suitLookup[card.getSuit()]))
			lines[5] += ('│         │ ')
			lines[6] += ('│         │ ')
			lines[7] += ('│ {0:>8}│ '.format(card.getName()))
			lines[8] += ('└─────────┘ ')
		
		# If it's the dealer, hide the second card
		if isDealer:
			lines[0] += ('┌─────────┐ ')
			lines[1] += ('│#########│ ')
			lines[2] += ('│#########│ ')
			lines[3] += ('│#########│ ')
			lines[4] += ('│#########│ '.format(suitLookup[card.getSuit()]))
			lines[5] += ('│#########│ ')
			lines[6] += ('│#########│ ')
			lines[7] += ('│#########│'.format(card.getName()))
			lines[8] += ('└─────────┘ ')

		
		_ = [print(line) for line in lines]
	
	def isBlackJack(self):
		"""
		Input:
			Nothing
		Action:
			Determine if this hand is blackjack or not
		Return:
			True if it is blackjack, False otherwise
		"""
		
		cards = self.getCards()
		
		# If we have a total of 21 in just 2 cards, this is BlackJack
		if len(cards) == 2 and self.getValue()[-1] == 21:
			return True
		
		return False
	
	def isBusted(self):
		"""
		Input:
			Nothing
		Action:
			Check if this hand has busted.
		Returns:
			Boolean True if busted, False otherwise
		"""
		
		# Just check if we have no more valid values
		if len(self.getValue()) == 0:
			return True
		
		return False
