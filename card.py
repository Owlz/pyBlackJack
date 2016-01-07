class Card:
	"""
	Defines what a playing card is.
	"""

	# Enums to make things sane
	enumName = {"A":[1,11],"2":[2], "3":[3], "4":[4], "5":[5], "6":[6], "7":[7], "8":[8], "9":[9], "10":[10], "J":[10], "Q":[10], "K":[10]}
	enumSuit = ["Diamond", "Spade", "Heart", "Club"]

	def __init__(self, name, suit):
		if name == None or suit == None:
			raise Exception("Attempted to create card without initial values")

		if name not in self.enumName or suit not in self.enumSuit:
			raise Exception("Invalid card creation of {0}:{1}".format(name,suit))

		# Setup the card

		# The name of the card (A,2..10,J,Q,K)
		self.name = name

		# Literal value of card represented as list
		# In case of Ace, this will be [1,11]
		self.value = self.enumName[name]

		self.suit = suit


	def getValue(self):
		"""
		Return the value for this card as a list
		Example: Ace = [1,11]
		"""

		# Making sure to return a copy, not a pointer to the real thing
		return self.value[:]

	def getName(self):
		"""
		Return the name of the card
		Example: "A"
		"""
		return self.name

	def getSuit(self):
		"""
		Returns the suit of this card
		Example: "Spade"
		"""
		return self.suit

	
	#def pretty(self):
	#	"""
	#	Returns a string containing the ASCII version of the card
	#	"""
		
	
