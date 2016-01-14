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
