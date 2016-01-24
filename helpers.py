def ofType(item, type):
	return item.__class__.__name__ == type

def asciiToBool(x):
	"""
	Input:
		String representation of boolean ("True","T","False","F","0","1")
	Action:
		Converts ascii of True/False into bool
	Returns:
		Converted string as boolean value
	"""

	x = x.lower()

	if x in ["true","t","1"]:
		return True
	elif x in ["false","f","0"]:
		return False
	else:
		raise Exception("Input to asciiToBool unknown conversion: {0}".format(x))

