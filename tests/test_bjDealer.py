# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from bjPlayer import Player
from bjHand import Hand
from bjDealer import Dealer
from bjUI import UI
from card import Card
from bjTable import Table

#with pytest.raises(Exception):
#	player.selectHandAction(0,allowedActions)

#monkeypatch.setattr(builtins,"input",lambda _: "p")

def test_allowedActions():
	"""
	Test out that we're allowing the correct actions
	"""
	
	# Create the player
	player = Player(money=100,name="John")

	# Create the UI
	ui = UI()

	# Get our rule set
	houseRules = ui.selectHouseRules("Mystic Lake -- Shakopee, MN")

	# Set up the dealer
	dealer = Dealer(houseRules=houseRules,ui=ui)

	#######
	# A/A #
	#######
	# Give the player a hand
	c1 = Card("A","Spade")
	c2 = Card("A","Diamond")
	hand = Hand(c1,c2)
	player.addHand(hand)

	# Figure out the allowed actions
	allowedActions = dealer.allowedHandActions(hand,player)

	# We should have the following actions
	assert allowedActions == {"hit","stand","double","split"}
	
	#######
	# 5/6 #
	#######
	player.clearHands()
	# Give the player a hand
	c1 = Card("5","Spade")
	c2 = Card("6","Diamond")
	hand = Hand(c1,c2)
	player.addHand(hand)

	# Figure out the allowed actions
	allowedActions = dealer.allowedHandActions(hand,player)

	# We should have the following actions
	assert allowedActions == {"hit","stand","double"}

	#########
	# 5/6/2 #
	#########
	player.clearHands()
	# Give the player a hand
	c1 = Card("5","Spade")
	c2 = Card("6","Diamond")
	c3 = Card("2","Diamond")
	hand = Hand(c1,c2)
	hand.addCard(c3)
	player.addHand(hand)

	# Figure out the allowed actions
	allowedActions = dealer.allowedHandActions(hand,player)

	# We should have the following actions
	assert allowedActions == {"hit","stand"}

def test_dealCardsToTable():
	"""
	Test dealing of cards to the table
	"""
	
	# Create the player
	player = Player(money=100,name="John")
	player2 = Player(money=100,name="Sue")

	# Create the UI
	ui = UI()

	# Get our rule set
	houseRules = ui.selectHouseRules("Mystic Lake -- Shakopee, MN")

	# Set up the table
	table = Table()
	table.addPlayer(player)
	table.addPlayer(player2)
	
	# We want to hit all these cases
	cases = {"Insurance":False,"NotInsurance":False,"BlackJack":False,"NotBlackJack":False}
	
	# TODO: Maybe change how I check these paths? Technically this could run indefinitely long :-/	
	while True:
		# Set up the dealer each time to ensure we don't run out of cards...
		dealer = Dealer(houseRules=houseRules,ui=ui)
		table.setDealer(dealer)

		# Clear the table
		table.reset()
		
		# Do the dealing
		insurance,blackjack = dealer.dealHandsToTable(table)
	
		# Basic sanity checks
		assert len(player.getHands()) == 1
		assert len(player2.getHands()) == 1
		assert len(dealer.getHands()) == 1
		assert len(player.getHand().getCards()) == 2
		assert len(player2.getHand().getCards()) == 2
		assert len(dealer.getHand().getCards()) == 2
		
		# Update our cases to track what we've seen
		cases["Insurance"] |= insurance
		cases["NotInsurance"] |= not insurance
		cases["BlackJack"] |= blackjack
		cases["NotBlackJack"] |= not blackjack
		
		# See if we've exercized every case yet
		if set(cases.values()) == {True}:
			break

def test_facilitatePlayerHand(monkeypatch):
	"""
	Test facilitatePlayerHand method
	"""
	# Create the UI
	ui = UI()

	# Get our rule set
	houseRules = ui.selectHouseRules("Mystic Lake -- Shakopee, MN")

	# Set up the dealer
	dealer = Dealer(houseRules=houseRules,ui=ui)
	
	#############
	# Hit/Stand #
	#############
	
	player = Player(money=100,name="Tim")
	hand = Hand(Card("2","Club"),Card("4","Club"))
	player.addHand(hand)
	
	# A little complicated player interaction here..
	def playerAction(x,y):
		global count
		# Player will hit then stand
		if count == 0:
			count += 1
			return "hit"
		else:
			return "stand"
	global count
	count = 0
	monkeypatch.setattr(player,"selectHandAction",playerAction)
	# Screw the UI here..
	monkeypatch.setattr(dealer.ui,"drawTable",lambda : None )
	
	dealer.facilitatePlayerHand(player,hand)
	
	# We should have 3 cards at this time
	assert len(hand.getCards()) == 3
	
	##########
	# Double #
	##########
	
	player = Player(money=100,name="Tim")
	hand = Hand(Card("2","Club"),Card("4","Club"))
	player.addHand(hand)
	
	# Double will need a bet
	player.placeBet(20)
	
	monkeypatch.setattr(player,"selectHandAction",lambda x,y : "double")
	
	dealer.facilitatePlayerHand(player,hand)

	# We should have 3 cards at this time
	assert len(hand.getCards()) == 3
	
	###########################
	# Double not enough money #
	###########################

	player = Player(money=100,name="Tim")
	hand = Hand(Card("2","Club"),Card("4","Club"))
	player.addHand(hand)

	# Double will need a bet
	player.placeBet(60)

	monkeypatch.setattr(player,"selectHandAction",lambda x,y : "double")
	
	with pytest.raises(Exception):
		dealer.facilitatePlayerHand(player,hand)

	# We should have 2 cards at this time
	assert len(hand.getCards()) == 2

	
	#######################
	# Split Unimplemented #
	#######################

	player = Player(money=100,name="Tim")
	hand = Hand(Card("A","Club"),Card("A","Spade"))
	player.addHand(hand)

	# Double will need a bet
	player.placeBet(40)

	monkeypatch.setattr(player,"selectHandAction",lambda x,y : "split")

	with pytest.raises(Exception):
		dealer.facilitatePlayerHand(player,hand)

	# We should have 2 cards at this time
	assert len(hand.getCards()) == 2

	###############
	# Busted Hand #
	###############

	player = Player(money=100,name="Tim")
	hand = Hand(Card("A","Club"),Card("K","Spade"))
	hand.addCard(Card("Q","Spade"))
	player.addHand(hand)

	# Double will need a bet
	player.placeBet(40)

	monkeypatch.setattr(player,"selectHandAction",lambda x,y : "hit")

	dealer.facilitatePlayerHand(player,hand)

	# We should be busted here
	assert len(hand.getValue()) == 0

