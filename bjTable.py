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
