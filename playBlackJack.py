#!/usr/bin/python3

import configparser
import string

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
	
# Welcome banner
printBanner()

# Get house rules to play by
houseRules = selectHouseRules()


