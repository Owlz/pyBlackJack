# Modularize the User Interface

import os
import configparser
import string

class UI():
	"""
	This class is used to modularize the user interface.
	Initially, the focus is on console. However, planning to incorporate graphical later.
	"""

	def printHouseRules(self,houseRules):
		"""
		Input:
			Rules object as defined from selectHouseRules call
		Action:
			Display the rules that are going to be in effect
		Returns:
			Nothing
		"""

		print("Number of decks per shoe:\t\t{0}".format(houseRules["number_of_decks"]))
		print("Dealer hits soft 17?:\t\t\t{0}".format(houseRules["hit_soft_17"]))
		print("Double allowed after split?:\t\t{0}".format(houseRules["double_after_split"]))
		print("Double allowed on what types of hands?: {0}".format(houseRules["double_on"]))
		print("Total number of hands allowed:\t\t{0}".format(houseRules["total_hands"]))
		print("Can you re-split Aces?:\t\t\t{0}".format(houseRules["resplit_ace"]))
		print("BlackJack pays:\t\t\t\t{0}".format(houseRules["blackjack_pays"]))
		print("Penetration:\t\t\t\t{0}\n".format(houseRules["penetration"]))


	def selectHouseRules(self,rulesName=None):
		"""
		Input:
			(optional) rulesName = If you know going into it what rule set you want to use (i.e.: "Mystic Lake -- Shakopee, MN")
		Action:
			Prompt user to select rule set the house will use (when to hit/stand, allow splits, etc)
			If rulesName specified, then just use that.
		Retuns: 
			Rule set dictionary object
		"""
		print("What rules would you like to play by? Type q to quit.")
	
		# Setup the config parser	
		ruleSets = configparser.ConfigParser()
	
		# Read the rules
		ruleSets.read('houseRules.ini')
	
		# If we happen to know already, just return it
		if rulesName != None:
			return ruleSets[rulesName]
		
		# Print the options
		for ruleSet in ruleSets:
			if ruleSet == "DEFAULT":
				continue
			print("{0:3}:  {1}".format(list(ruleSets).index(ruleSet),ruleSet))
	
		i = "x"
		# Loop until we get good input	
		while i not in string.digits and i not in ['Q','q']:
	
			# Get input
			i = input("\nSelect RuleSet: ")
	
		# If we're quiting	
		if i in ['Q','q']:
			print('Bye!')
			exit(0)
	
		return ruleSets[list(ruleSets)[int(i,10)]]

	
	def clearScreen(self):
		"""
		Simple function to clear the screen.
		"""
		os.system('cls' if os.name == 'nt' else 'clear')
	
	def getTable(self):
		"""
		Input:
			Nothing
		Action:
			Retrieve Table object
		Returns:
			Table object for this UI
		"""
		return self.table

	def drawAsciiTable(self):
		"""
		Input:
			table = Table object
		Action:
			Draw out ASCII interface
		Returns:
			Nothing
		"""
	
		self.clearScreen()
	
		print("Dealer's Hand")
		print("-------------")
		self.getTable().getDealer().getHand().pprint(isDealer=(not self.getTable().getDealer().dealerTurn))
		# Only show this info on the dealer's turn
		if self.getTable().getDealer().dealerTurn:
			hand = self.getTable().getDealer().getHand()
			if hand.isBlackJack():
				print("BlackJack!")
			elif not hand.isBusted():
				print("Total: {0}".format(' or '.join([str(x) for x in hand.getValue()])))
			else:
				print("Busted!")
		
		for player in self.getTable().getPlayers():
			h = 1
			print("")
			heading = "{0} (${1})".format(player.name,player.money)
			heading += "\n" + "-"*len(heading)
			print(heading)
			for hand in player.getHands():
				print("")
				heading = "Hand {0} (${1})".format(h,player.getBets()[player.getHands().index(hand)])
				heading += "\n" + "-"*len(heading)
				print(heading)
				h += 1
				# Prettyprint it
				hand.pprint()
				if hand.isBlackJack():
					print("BlackJack!")
				elif not hand.isBusted():
					print("Total: {0}".format(' or '.join([str(x) for x in player.getHand().getValue()])))
				else:
					print("Busted!")

	def __init__(self,table=None,version="console"):
		"""
		Input:
			(optional) table == Table object that will be the focus of the UI
			(optional) version == what type of UI to use. Defaults to console.
		Action:
			Setup UI to use the given type
		Returns:
			Instance of the UI
		
		Instance variables include: version, table
		"""
		
		self.version = version
		
		self.table = table
	
	def drawTable(self):
		"""
		Input:
			None
		Action:
			Re-Draw the screen. Generic so that it can be called by anything.
		Returns:
			Nothing
		"""
		
		if self.version == "console":
			self.drawAsciiTable()
		
		else:
			raise Exception("Haven't implemented drawing of {0} yet".format(self.version))

