numbersList = [2,20,0,4,1,17]

def spokenNbAt(number):
	for i in range(0, number):
		if (i >= len(numbersList)):
				newValue = hasBeenSpoken(numbersList[i-1])
				numbersList.append(newValue)
	return numbersList[-1]

def hasBeenSpoken(number):
	found = False
	remember = 0
	for i in range(0, len(numbersList)-1):
		if (numbersList[i] == number):
			remember = i
			found = True
	if (found):
		return len(numbersList)-(remember+1)
	return 0

print(spokenNbAt(2020))