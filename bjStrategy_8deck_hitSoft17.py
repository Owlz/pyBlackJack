"""
	This strategy is optimized for the following rules:
	Decks: 8
	Dealer Hit Soft 17: Yes
	Surrender: No
	Double Down: Only for first card

	To be a valid strategy class it must export "strategy".
"""


def strategy(hand, upcard, bet, bankroll):
	"""
	Determine what to do based on these factors
	hand == Python bjHand object
	upcard == Python card object for dealer's up-card
	bet == Dollar amount that was wagered
	bankroll == How much money the user has (this is minus the current bet)
	Returns: Hit, Stand, or Double
	"""

	# Highest value for the hand. If an Ace is involved, return the highest value without going over 21
	total = hand.getValue().pop()

	# Dealer's upcard value
	up = upcard.getValue().pop()

	# Do we want to double down?
	double = False

	# Define if we're looking at a Hard or Soft value
	if len(hand.getValue()) > 1:
		soft = True
	else:
		soft = False

	# If our total is 8 or less, take a hit
	if total <= 8:
		return "Hit"

	if total == 21:
		return "Stand"

	##############
	# Soft Total
	##############
	if soft:
		# A,9 or A,8
		if total == 20 or total == 19:
			return "Stand"

		# A,7
		if total == 18:

			if up in [2,3,7]:
				return "Stand"

			if up in [8,9,10,11]:
				return "Hit"

			if up in [4,5,6]:
				double = True

		# A, 6
		if total == 17:

			if up in [2,3,4,5,7,8,9,10,11]:
				return "Hit"

			else:
				double = True

	##############
	# Hard Total
	##############
	if not soft:

		# If our total is 17 or more hard, stand
		if total >= 17 and not soft:
			return "Stand"

		if total == 9 and up in [2, 3, 7, 8, 9, 10, 11]:
			return "Hit"

		if total == 9 and up in [4, 5, 6]:
			if soft:
				double = True
			else:
				return "Hit"
	
		if total == 10 and up in [2, 3, 4, 5, 6, 7, 8]:
			if soft:
				double = True
			else:
				return "Hit"

		if total == 10 and up in [9, 10, 11]:
			return "Hit"

		if total == 11 and up in [2, 3, 4, 5, 6, 7, 8, 9]:
			if soft:
				double = True
			else:
				return "Hit"

		if total == 11 and up in [10, 11]:
			return "Hit"
	
		if total in range(12,20) and up in range(2,7):
			return "Stand"

		if total in range(12,15) and up in range(7, 12):
			return "Hit"

		if total == 15 and up in [7, 8, 9, 11]:
			return "Hit"

		if total == 15 and up == 10:
			return "Stand"

		if total == 16 and up in [7, 8]:
			return "Hit"

		if total == 16 and up in [9, 10, 11]:
			return "Stand"


	# If we're looking at a soft value
	if soft:
		pass

	#hand.printCards()
	#print "\n"

	# If we're here, the only reason should be that we want to double
	assert double

	# Case where we want to double, make sure we have the funds
	if double and bankroll >= bet:
		return "Double"

	# If we're here, then we can't double due to funds and should just hit
	return "Hit"


