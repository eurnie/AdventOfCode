import copy

def simulateGame(inputString, rounds):
	newString = copy.deepcopy(inputString)
	for i in range(0, rounds):
		newString = simulateRound(newString)
	positionOfOne = newString.find('1')
	return newString[positionOfOne+1:] + newString[:positionOfOne]

def simulateRound(inputString):
	newString = copy.deepcopy(inputString)
	takeOut = newString[1:4]
	newString = newString[0] + newString[4:]
	newPositionNumberFound = False
	newPositionNumber = int(newString[0])
	while (not newPositionNumberFound):
		if (newPositionNumber == 0):
			newPositionNumber = 9
		else:
			newPositionNumber -= 1
		if (str(newPositionNumber) in newString):
			newPositionNumberFound = True
	location = newString.find(str(newPositionNumber))
	newString = newString[:location+1] + takeOut + newString[location+1:]
	return newString[1:] + newString[0]

print(simulateGame('193467258', 100))