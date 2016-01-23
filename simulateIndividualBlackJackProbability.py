from bjhand import *
from card import *
from shoe import *
from random import randint
import sys
from bjStrategy_8deck_hitSoft17 import strategy


if len(sys.argv) != 9:
	print("Usage: " + sys.argv[0] + " <nDecks> <dealerUpCard> <userTotal> <# of simulations> <playerAction \"Hit\"/\"Stand\"> <hitSoft17: 0|1>i <isSoftTotal: 0|1> <oneHit: 0|1>\n")
	exit(0)


"""
# Define variables
nDecks = 8
dealerUpCard = "4"
userTotal = 12
# Number of times to run the simulation
run = 200000
# player Action == Stand/Hit (Split not implemented yet)
#playerAction = "Hit"
playerAction = "Stand"
hitSoft17 = True
"""

# Define variables
nDecks = int(sys.argv[1])
dealerUpCard = sys.argv[2]
userTotal = int(sys.argv[3])
# Number of times to run the simulation
run = int(sys.argv[4])
# player Action == Stand/Hit (Split not implemented yet)
#playerAction = "Hit"
#playerAction = "Stand"
playerAction = sys.argv[5]
#hitSoft17 = True
hitSoft17 = bool(int(sys.argv[6])) 
isSoftTotal = bool(int(sys.argv[7]))
oneHit = bool(int(sys.argv[8]))

###################

print("Test case:\nNumber of Decks: {0}\nDealer up card: {1}\nUser Total: {2}\nNumber of test hands: {3}\nPlayer Action: {4}\nHitSoft17: {5}\nIsSoftTotal: {6}\nOne Hit: {7}\n".format(nDecks, dealerUpCard, userTotal, run, playerAction, hitSoft17, isSoftTotal, oneHit))

def dealerPlay():
	# Play the dealer's hand
	# Return's dealer's final value
	global s, dHand

	while True:
		# Check if the dealer has busted
		if len(dHand.getValue()) == 0:
			return 0

		dVal = dHand.getValue().pop()
		#print "\nDealer's Hand: {0}".format(dVal)
		#dHand.printCards()

		# Always hit under 17
		if dVal < 17:
			dHand.addCard(s.dealCard())
			continue

		# Always staying above 17
		if dVal > 17:
			return dVal


		# If we're here, we're at 17

		# If we have more than 1 value, we're a soft 17
		if hitSoft17 and len(dHand.getValue()) > 1:
			dHand.addCard(s.dealCard())
			continue

		return dVal


def userPlay():
	global pHand, dHand, s

	#pHand.printCards()
	#print "\n"

	# Hit until we're satisfied
	while strategy(pHand, dHand.getCards().pop(), 1, 100) in ["Hit","Double"]:
		# Deal the player another card
		pHand.addCard(s.dealCard())

		#pHand.printCards()
		#print "\n"

		if len(pHand.getValue()) == 0:
			return
	


##################
win = 0.
loss = 0.
push = 0.

while run > 0:
	run -= 1

	s = Shoe(nDecks)
	pHand = Hand()
	dHand = Hand(s.dealSpecificCard(dealerUpCard))

	# If we're not playing a soft total hand
	if not isSoftTotal:
		# Make the user total
		if userTotal <= 12:
			c1 = randint(2,userTotal - 2)
		else:
			c1 = randint(userTotal-10,10)
		c2 = userTotal - c1

	# If we are playing a soft total hand
	else:
		assert userTotal - 11 > 0
		c1 = "A"
		c2 = userTotal - 11

		# In the case we're testing A,A
		if c2 == 1:
			c2 = "A"


	# Give the user his hand
	pHand.addCard(s.dealSpecificCard(str(c1)))
	pHand.addCard(s.dealSpecificCard(str(c2)))

	# Shuffle the shoe
	s.shuffle()

	#print "User hand total: {0}".format(pHand.getValue().pop())
	#pHand.printCards()
	#print "\n"

	if playerAction == "Hit":
		pHand.addCard(s.dealCard())
		#print "\nUser hand total: {0}".format(pHand.getValue())
		#pHand.printCards()
		#print "\n"

		# Player busted
		if len(pHand.getValue()) == 0:
			#print "Player bust"
			loss += 1
			continue

		if not oneHit:
			# Continue playing with the normal
			userPlay()

			# See if we busted
			if len(pHand.getValue()) == 0:
				loss += 1
				continue

	p = pHand.getValue().pop()

	d = dealerPlay()
	#print "\nDealer final: {0}".format(d)

	# If the player won
	if p > d:
		win += 1
		#print "Win\n"
		continue

	# If the dealer won
	if d > p:
		loss += 1
		#print "Lose\n"
		continue

	# Looks like a push
	push += 1
	continue

print("Win: {0}\nLoss: {1}\nPush: {2}\nWinning Probability: {3}\n\n".format(win, loss, push, (win/(win+loss+push))))
