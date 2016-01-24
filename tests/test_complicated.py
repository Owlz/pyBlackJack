# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from bjPlayer import Player
from bjDealer import Dealer
from bjTable import Table
from bjUI import UI
from card import Card
import builtins
from bjHand import Hand

def test_selectHandActionUser(monkeypatch):
	"""
	Testing selecting a Hand's action
	"""
	
	# Create the player
	player = Player(money=100,name="John")
	
	# Create the UI
	ui = UI()
	
	# Get our rule set
	houseRules = ui.selectHouseRules("Mystic Lake -- Shakopee, MN")
	
	# Set up the dealer
	dealer = Dealer(houseRules=houseRules,ui=ui)
	
	# Give the player a hand
	c1 = Card("A","Spade")
	c2 = Card("A","Diamond")
	hand = Hand(c1,c2)
	player.addHand(hand)
	
	# Figure out the allowed actions
	allowedActions = dealer.allowedHandActions(hand,player)
	
	# We should have the following actions
	assert allowedActions == {"hit","stand","double","split"}
	
	# Test split
	monkeypatch.setattr(builtins,"input",lambda _: "p")
	action = player.selectHandAction(0,allowedActions)
	assert action == "split"
	
	# Test hit
	monkeypatch.setattr(builtins,"input",lambda _: "h")
	action = player.selectHandAction(0,allowedActions)
	assert action == "hit"

	# Test stand
	monkeypatch.setattr(builtins,"input",lambda _: "s")
	action = player.selectHandAction(0,allowedActions)
	assert action == "stand"

	# Test double
	monkeypatch.setattr(builtins,"input",lambda _: "d")
	action = player.selectHandAction(0,allowedActions)
	assert action == "double"

	# Test error
	allowedActions.remove("split")
	monkeypatch.setattr(builtins,"input",lambda _: "p")
	with pytest.raises(Exception):
		player.selectHandAction(0,allowedActions)
	
	# Test non-human
	# TODO: Need to do this better. This is hackish
	player.isInteractive = False
	with pytest.raises(Exception):
		player.selectHandAction(0,allowedActions)
