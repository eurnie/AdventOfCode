numbersList = [2,20,0,4,1,17]
numbersDictionary = {}

def spokenNbAt(number):
	for number2 in numbersList:
		numbersDictionary[number2] = numbersList.index(number2) + 1

	for i in range(0, number):
		if (i >= len(numbersList)):
			newValue = hasBeenSpoken(previousValue, i + 1)
			numbersDictionary[previousValue] = i
			previousValue = newValue
		else:
			previousValue = numbersList[i]
	return newValue

def hasBeenSpoken(number, time):
	if number in numbersDictionary:
		value = numbersDictionary[number]
		if (value != time-1):
			return (time - value - 1)
	return 0

print(spokenNbAt(30000000))