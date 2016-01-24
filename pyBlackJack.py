#!/usr/bin/python3

from bjDealer import Dealer
from bjPlayer import Player
from bjHand import Hand
from bjTable import Table
from bjUI import UI
import os

def clearScreen():
	"""
	Simple function to clear the screen.
	"""
	os.system('cls' if os.name == 'nt' else 'clear')


def printBanner():
	"""
	Print out "pyBlackJack" in ASCII art characters
	"""
	clearScreen()
	
	print(""".------..------..------..------..------..------..------..------..------..------..------.
|P.--. ||Y.--. ||B.--. ||L.--. ||A.--. ||C.--. ||K.--. ||J.--. ||A.--. ||C.--. ||K.--. |
| :/\: || (\/) || :(): || :/\: || (\/) || :/\: || :/\: || :(): || (\/) || :/\: || :/\: |
| (__) || :\/: || ()() || (__) || :\/: || :\/: || :\/: || ()() || :\/: || :\/: || :\/: |
| '--'P|| '--'Y|| '--'B|| '--'L|| '--'A|| '--'C|| '--'K|| '--'J|| '--'A|| '--'C|| '--'K|
`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'`------'

""")

# Init the table
table = Table()

# Create UI
ui = UI(table)

# Welcome banner
printBanner()

# Get house rules to play by
houseRules = ui.selectHouseRules()

ui.printHouseRules(houseRules)

name = input("What's your name?: ")
money = input("How much money to start with?: ")

player = Player(money=money,name=name)

# Add the player to the table
table.addPlayer(player)

# Init our dealer
dealer = Dealer(houseRules=houseRules,ui=ui)

# Add him to the table
table.addDealer(dealer)

while True:
	# Get the table ready
	table.reset()
	
	# Get the wager
	table.placeBets()
	
	# Deal to the table
	insurance, dealerBlackJack = dealer.dealHandsToTable(table)
	
	ui.drawTable()
	#drawAsciiTable(table,showDealerCard=False)
	
	if insurance:
		print("Insurance?")
	
	# If the dealer has blackjack	
	if dealerBlackJack:
		print("Dealer Has BlackJack")
		table.getDealer().payoutTable(table)
		table.getDealer().dealerTurn = True
		ui.drawTable()
		continue
	
	#validActions = dealer.allowedHandActions(player.getHand(),player)
	#player.selectHandAction(0,validActions)
	table.playActiveHands()
	
	ui.drawTable()
	
	table.getDealer().payoutTable(table)
