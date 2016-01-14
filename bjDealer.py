from bjShoe import Shoe

class Dealer:
	"""
	Class acts to abstract the things that a dealer would do
	"""
	
	def asciiToBool(self,x):
		"""
		Input:
			String representation of boolean ("True","T","False","F","0","1")
		Action:
			Converts ascii of True/False into bool
		Returns:
			Converted string as boolean value
		"""
		
		x = x.lower()	
		
		if x in ["true","t","1"]:
			return True
		elif x in ["false","f","0"]:
			return False
		else:
			raise Exception("Input to asciiToBool unknown conversion: {0}".format(x))
	
	def blackJackPaysToInt(self,x):
		"""
		Input:
			x = Ascii representation of what blackjack pays (such as "3:2" or "6:5")
		Action:
			Convert string into integer. Example: "3:2" would convert to 1.5
		Return:
			Integer for use in calculating blackjack payout
		"""
		
		# Split the numbers apart
		num, den = map(int,"3:2".split(":"))
		
		# Return the result
		return num/den

	def __init__(self, houseRules):
		"""
		houseRules = object of rules as returned by "selectHouseRules"
		"""
		
		self.numDecksPerShoe = int(houseRules["number_of_decks"],10)
		
		self.hitSoft17 = self.asciiToBool(houseRules["hit_soft_17"])
		
		self.doubleAfterSplit = self.asciiToBool(houseRules["double_after_split"])
		
		# TODO: Not sure how to deal with this one. Probably need an enum.
		self.doubleOn = houseRules["double_on"]
		
		self.totalHandsAllowed = int(houseRules["total_hands"],10)
		
		self.resplitAces = self.asciiToBool(houseRules["resplit_ace"])
		
		self.blackJackPays = self.blackJackPaysToInt(houseRules["blackjack_pays"])
		
		self.penetration = float(houseRules["penetration"])
		
		# Init a new Shoe while we're at it
		self.shoe = Shoe(self.numDecksPerShoe)
		self.shoe.shuffle()

	def dealCardToHand(self,hand,numCards=1):
		"""
		Input:
			hand = Hand object that we should deal to
			(optional) numCards = integer number of cards to deal. 2 would be used to deal a new hand out.
		Action:
			Pops a card from the top of shoe stack and adds it to the hand object
		Return:
			Nothing. The object is mutable and changed in place to save memory and increase speed.
		"""
		
		# Bastardizing this a little to quickly deal any number of cards out
		for x in range(numCards):
			hand.addCard(self.shoe.dealCard())
