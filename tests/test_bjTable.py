# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from bjTable import Table
from bjPlayer import Player
from bjUI import UI
from bjDealer import Dealer
from bjHand import Hand
from card import Card

#with pytest.raises(Exception):
#	player.selectHandAction(0,allowedActions)

#monkeypatch.setattr(builtins,"input",lambda _: "p")

def test_placeAndClearBets(monkeypatch):
	"""
	Testing placing and clearing bets
	"""
		
	table = Table()
	player = Player(money=100,name="Steve")
	player2 = Player(money=100,name="Bob")
	
	table.addPlayer(player)
	table.addPlayer(player2)
	
	# Need to monkeypatch input
	#global count = 0
	def placeBet():
		global count
		if count == 0:
			count += 1
			self.placeBet(10)
		else:
			self.placeBet(20)
	
	# Since we're basically changing the call variables
	# we need to copy the original method and call it separately
	player.placeBetOriginal = player.placeBet
	player2.placeBetOriginal = player2.placeBet	
	monkeypatch.setattr(player,"placeBet",lambda : player.placeBetOriginal(10))
	monkeypatch.setattr(player2,"placeBet",lambda : player2.placeBetOriginal(20))
	
	# Place the bets
	table.placeBets()
	
	# Test that it worked
	assert len(player.getBets()) == 1
	assert player.getBets()[0] == 10
	assert len(player2.getBets()) == 1
	assert player2.getBets()[0] == 20
	
	# Now clear them
	table.clearBets()
	
	assert len(player.getBets()) == 0
	assert len(player2.getBets()) == 0

def test_playActiveHands(monkeypatch):
	"""
	Testing playing active hands
	"""
	
	# Create the table
	table = Table()

	# Create the UI
	ui = UI(table)

	# Get our rule set
	houseRules = ui.selectHouseRules("Mystic Lake -- Shakopee, MN")

	# Set up the dealer (don't waste time between cards)
	dealer = Dealer(houseRules=houseRules,ui=ui,dealCardDelay=0)

	# Set up the players
	player = Player(money=100,name="Ted")
	player2 = Player(money=100,name="James")
	
	# Add to table
	table.addPlayer(player)
	table.addPlayer(player2)
	table.setDealer(dealer)
	
	# Add hands
	hand = Hand(Card("5","Club"),Card("5","Spade"))
	hand2 = Hand(Card("6","Club"),Card("7","Diamond"))
	player.addHand(hand)
	player.addHand(hand2)
	
	hand3 = Hand(Card("A","Spade"),Card("7","Club"))
	player2.addHand(hand3)
	
	hand4 = Hand(Card("5","Diamond"),Card("7","Spade"))
	dealer.addHand(hand4)
	
	# Interaction here can get ugly. We're only going to test
	# How many times we get our hands run
	def countHands(x,y):
		global count
		count += 1
	
	global count
	count = 0
	
	# Add the monkeypatch
	monkeypatch.setattr(dealer,"facilitatePlayerHand",countHands)
	monkeypatch.setattr(dealer,"playDealersHand",lambda _: None)
	
	# Try it out
	table.playActiveHands()
	
	# Make sure we did all hands	
	assert count == 3

