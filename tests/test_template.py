# The following 3 lines are necessary to import correctly
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest

#with pytest.raises(Exception):
#	player.selectHandAction(0,allowedActions)

#monkeypatch.setattr(builtins,"input",lambda _: "p")

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
"""
