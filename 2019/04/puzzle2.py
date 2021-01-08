def calculateNbOfPasswords(min, max):
	counter = 0
	for x in range(min, max+1):
		if (checkDigitsRule(x)):
			counter += 1
	return counter

def checkDigitsRule(number):
	numberString = str(number)
	isSequence = (False, 0)
	hasAdjacent = (False, 0)
	beforeLast = 0
	last = 0
	for x in range(0, len(numberString)):
		if (int(numberString[x]) != isSequence[1]):
			isSequence = (False, 0)
		if (int(numberString[x]) < last):
			return False
		if (int(numberString[x]) == last) and (not isSequence[0]):
			if (int(numberString[x]) == beforeLast):
				if (hasAdjacent[0]) and (hasAdjacent[1] == int(numberString[x])):
					hasAdjacent = (False, 0)
				isSequence = (True, int(numberString[x]))
			else:
				if (not hasAdjacent[0]):
					hasAdjacent = (True, int(numberString[x]))
		beforeLast = last
		last = int(numberString[x])
	if (hasAdjacent[0]):
		return True 
	return False

print(calculateNbOfPasswords(387638, 919123))