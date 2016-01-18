from bjShoe import Shoe
from bjPlayer import Player

class Dealer(Player):
	"""
	Class acts to abstract the things that a dealer would do
	We're extending Player as Dealers are a subset of players
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
		
		# Give ourself a hands list
		self.hands = []

	def allowedHandActions(self,hand,player):
		"""
		Input:
			hand == Hand class instance
			player == Player class instance
		Action:
			Determines valid actions that the player can take with the given hand
		Returns:
			Set of allowed actions. Possible actions include "hit","stand","double","split","surrender"
		"""
		
		# TODO: Double after split
		
		# TODO: doubleOn
		
		# TODO: totalHandsAllowed
		
		# TODO: resplitAces
		
		actions = {"hit","stand"}
		
		# Grab the cards
		cards = hand.getCards()
		
		# If this is our first two, we have more options
		if len(cards) == 2:
			# We can double any two first cards
			actions = actions.union({"double"})
			
			# We can split any first two cards that are the same
			if cards[0].getName() == cards[1].getName():
				actions = actions.union({"split"})
		
		return actions


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
	
	def dealHandsToTable(self,table):
		"""
		Input:
			table == Table object
		Action:
			Deals a full hand to each player at the table (one at a time as you would in a Casino
		Returns:
			(insurance, dealerBlackJack)
			insurance == Do we need to ask players for insurance (meaning, Dealer is showing an Ace)
			dealerBlackJack == dealer has BlackJack
		"""
		
		# Need to do this twice because everyone gets 2 cards
		for x in range(2):	
			# Loop through all the players
			for player in table.getPlayers():
				self.dealCardToHand(player.getHand())
			
			# Don't forget our own hand!
			self.dealCardToHand(self.getHand())
		
		# Check for blackjacks and insurance stuff here
		if self.getHand().getCards()[0].getName() == "A":
			insurance = True
		else:
			insurance = False
		
		# Check for dealer blackjack
	
		return insurance, self.getHand().isBlackJack()
