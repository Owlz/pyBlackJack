# Modularize the User Interface

import os

class UI():
	"""
	This class is used to modularize the user interface.
	Initially, the focus is on console. However, planning to incorporate graphical later.
	"""
	
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

