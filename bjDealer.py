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
	
	def __init__(self, houseRules):
		"""
		houseRules = object of rules as returned by "selectHouseRules"
		"""
		
		self.numDecksPerShoe = int(houseRules["number_of_decks"],10)
		self.hitSoft17 = houseRules["hit_soft_17"]
		self.doubleAfterSplit = houseRules["double_after_split"]
		self.doubleOn = houseRules["double_on"]
		self.totalHandsAllowed = houseRules["total_hands"]
		self.resplitAces = houseRules["resplit_ace"]
		self.blackJackPays = houseRules["blackjack_pays"]
