class Table():
	"""
	A BlackJack Table just contains a bunch of players. Omitting the Dealer position for this class.
	"""
	
	def __init__(self):
		# Init the players
		self.players = []
		
		# Init the dealer
		self.dealer = None
	
	def addPlayer(self,player):
		"""
		Input:
			player = bjPlayer object
		Action:
			Add player to the blackjack table
		Returns:
			Nothing
		"""
		self.players.append(player)
	
	def getPlayers(self):
		"""
		Input:
			None
		Action:
			Return list of players
		Returns:
			List of players
		"""
		return self.players
	
	def setDealer(self,dealer):
		"""
		Input:
			dealer = Dealer object
		Action:
			Sets dealer to the table
		Returns:
			Nothing
		"""
		
		self.dealer = dealer
	
	def getDealer(self):
		"""
		Input:
			None
		Action:
			Get Dealer object for this table
		Returns:
			Dealer object for this table
		"""
		return self.dealer
	
	def clearBets(self):
		"""
		Input:
			None
		Action:
			Clears wagers for all players at the table.
		Returns:
			Nothing
		"""
		
		# Just loop through the players and clear their bets.	
		for player in self.getPlayers():
			player.clearBet()
	
	def placeBets(self):
		"""
		Input:
			None
		Action:
			Gets wagers from players for their hands.
			Actually just calls "placeBet" for each player at the table.
		Returns:
			Nothing
		"""
		
		# Loop through the players and let the player object take care of bets
		for player in self.getPlayers():
			player.placeBet()
	
	def playActiveHands(self):
		"""
		Input:
			None
		Action:
			Go through all players, allow each to play their hands in turn.
			Includes playing the dealer's hand
		Return:
			Nothing
		"""
		
		# Loop through players
		for player in self.getPlayers():
			# Loop through all their hands
			for hand in player.getHands():
				# Call dealer method to handle it
				self.getDealer().facilitatePlayerHand(player,hand)
		
		# Play the dealer's hand
		self.getDealer().playDealersHand(self)
		
		
	def getNumActiveHands(self):
		"""
		Input:
			Nothing
		Action:
			Determine the number of active hands at the table
		Returns:
			Number of active hands at the table, as an integer value
		"""
		# TODO: I'm pretty sure I can make this faster with comprehensions or Map
		
		# Here's the count
		numHands = 0
		
		# Get the players
		for player in self.getPlayers():
			# Get the hands
			for hand in player.getHands():
				if not hand.isBusted():
					numHands += 1
		
		return numHands
	
	def reset(self):
		"""
		Input:
			Nothing
		Action:
			Clears all player's bets and hands.
			Creates blank hands for all players
			Basically, gets the table ready for another round.
		Returns:
			Nothing
		"""
		
		# Loop through all players
		for player in self.getPlayers():
			player.clearBets()
			player.clearHands()
			player.addHand()
		
		# Don't forget the dealer's hand
		self.getDealer().clearHands()
		self.getDealer().addHand()
		
		# Also, it's no longer the dealers turn!
		self.getDealer().dealerTurn = False
