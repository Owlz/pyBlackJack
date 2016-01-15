#!/usr/bin/python3

import configparser
import string
from prettytable import PrettyTable
from bjDealer import Dealer
from bjPlayer import Player
from bjHand import Hand
from bjTable import Table
import os

def printBanner():
	"""
	Print out "pyBlackJack" in ASCII art characters
	"""
	print(""".------..------..------..------..------..------..------..------..------..------..------.
|P.--. ||Y.--. ||B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :/\: || (\/) || :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| (__) || :\/: || ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'P|| '--'Y|| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'

""")

def printHouseRules(houseRules):
	"""
	Input:
		Rules object as defined from selectHouseRules call
	Action:
		Display the rules that are going to be in effect
	Returns:
		Nothing
	"""
	
	t = PrettyTable(["Name", "Value"])
	
	print("Number of decks per shoe:\t\t{0}".format(houseRules["number_of_decks"]))
	print("Dealer hits soft 17?:\t\t\t{0}".format(houseRules["hit_soft_17"]))
	print("Double allowed after split?:\t\t{0}".format(houseRules["double_after_split"]))
	print("Double allowed on what types of hands?: {0}".format(houseRules["double_on"]))
	print("Total number of hands allowed:\t\t{0}".format(houseRules["total_hands"]))
	print("Can you re-split Aces?:\t\t\t{0}".format(houseRules["resplit_ace"]))
	print("BlackJack pays:\t\t\t\t{0}".format(houseRules["blackjack_pays"]))
	print("Penetration:\t\t\t\t{0}\n".format(houseRules["penetration"]))
	

def selectHouseRules():
	"""
	Input:
		None
	Action:
		Prompt user to select rule set the house will use (when to hit/stand, allow splits, etc)
	Retuns: 
		Rule set dictionary object
	"""
	print("What rules would you like to play by? Type q to quit.")

	# Setup the config parser	
	ruleSets = configparser.ConfigParser()
	
	# Read the rules
	ruleSets.read('houseRules.ini')
	
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

def drawAsciiTable(table):
	"""
	Input:
		table = Table object
	Action:
		Draw out ASCII interface
	Returns:
		Nothing
	"""
	
	print("Dealer's Hand")
	print("-------------")
	table.getDealer().getHand().pprint(isDealer=True)
	
	for player in table.getPlayers():
		h = 1
		for hand in player.getHands():
			print("")
			heading = "{0}'s Hand {1}".format(player.name,h)
			heading += "\n" + "-"*len(heading)
			print(heading)
			h += 1
			table.getPlayers()[0].getHand().pprint()
	

# Welcome banner
printBanner()

# Get house rules to play by
houseRules = selectHouseRules()

printHouseRules(houseRules)

name = input("What's your name?: ")
money = input("How much money to start with?: ")

player = Player(money=money,name=name)

# Clear the screen
os.system('cls' if os.name == 'nt' else 'clear')

# Init the table
table = Table()

# Add the player to the table
table.addPlayer(player)

# Init our dealer
dealer = Dealer(houseRules)

# Give the dealer a hand
dealer.addHand()

# Add him to the table
table.addDealer(dealer)

# Give the player a hand
player.addHand()

# Deal to the table
dealer.dealHandsToTable(table)

drawAsciiTable(table)
