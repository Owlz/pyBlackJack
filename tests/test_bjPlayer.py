# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
from bjPlayer import Player
from helpers import *
from bjHand import Hand
from card import Card
from bjDealer import Dealer
import builtins

def test_initialization():
	"""
	Create a player object in a few different ways
	"""
	
	p = Player(money=100)
	p = Player(money=100,strategy="bjStrategy_8deck_hitSoft17")
	p = Player(money=100,name="Bill")
	p = Player(money=100,strategy="bjStrategy_8deck_hitSoft17",name="Steve")

def test_getMoney():
	"""
	Testing the getMoney call
	"""
	
	p = Player(money=167)
	assert p.getMoney() == 167

def test_addMoney():
	"""
	Testing adding and removing money
	"""
	
	p = Player(money=100)
	p.addMoney(5)
	assert p.getMoney() == 105
	
	p.addMoney(-6)
	assert p.getMoney() == 99

def test_isHuman():
	"""
	Testing isHuman call
	"""
	
	# Implicitly is human
	p = Player(money=100,name="Steve")
	assert p.isHuman()
	
	# Adding a strategy makes this non-human
	p = Player(money=100,strategy="bjStrategy_8deck_hitSoft17",name="Jenni")
	assert not p.isHuman()

def test_addAndGetHand():
	"""
	Testing adding of a hand object
	"""
	
	p = Player(money=100)

	# Add a blank hand
	p.addHand()
	
	# Make sure we got it
	assert len(p.getHands()) == 1
	
	# Get it specifically
	h = p.getHand()
	assert ofType(h,"Hand")
	
	h = Hand()
	p.addHand(h)
	
	assert len(p.getHands()) == 2
	assert ofType(p.getHand(1),"Hand")

	with pytest.raises(AssertionError):
		p.addHand("Blerg")
	
	p.clearHands()
	assert len(p.getHands()) == 0
	

def test_betting(monkeypatch):
	"""
	Testing different things we can do with betting
	"""
	p = Player(money=100)
	# Basic bet
	p.placeBet(10)
	
	# Test placing a negative bet
	with pytest.raises(Exception):
		p.placeBet(-10)
	
	# Test betting more than we have
	with pytest.raises(Exception):
		p.placeBet(100)
	
	# Need to monkeypatch the input
	monkeypatch.setattr(builtins,"input",lambda _: "5")
	
	# This should call User input, which we just defined as returning 5
	p.placeBet()
	
	# Get the bets
	bets = p.getBets()
	
	# We have had 2 bets so far	
	assert len(bets) == 2
	
	# Clear the bets
	p.clearBets()
	assert len(p.getBets()) == 0
	
	# Create a machine user
	p = Player(money=100,strategy="bjStrategy_8deck_hitSoft17")
	
	# For now this should create an exception
	with pytest.raises(Exception):
		p.placeBet()
	
