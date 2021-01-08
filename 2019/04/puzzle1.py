def calculateNbOfPasswords(min, max):
	counter = 0
	for x in range(min, max+1):
		if (checkDigitsRule(x)):
			counter += 1
	return counter

def checkDigitsRule(number):
	numberString = str(number)
	hasAdjacent = False
	last = 0
	for x in range(0, len(numberString)):
		if (int(numberString[x]) < last):
			return False
		if (int(numberString[x]) == last):
			hasAdjacent = True
		last = int(numberString[x])
	if (hasAdjacent):
		return True 
	return False

print(calculateNbOfPasswords(387638, 919123))