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
	
	def addDealer(self,dealer):
		"""
		Input:
			dealer = Dealer object
		Action:
			Adds dealer to the table
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
