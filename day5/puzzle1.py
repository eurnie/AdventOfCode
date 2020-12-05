def getLowerHalf(tuple):
	min = tuple[0]
	max = tuple[1]
	if ((max - min) == 1):
		return (min, min)
	else:
		newMax = min + (round((max - min) / 2) - 1)
		return (min, newMax)		

def getUpperHalf(tuple):
	min = tuple[0]
	max = tuple[1]
	if ((max - min) == 1):
		return (max, max)
	else:
		newMin = min + (round((max - min) / 2))
		return (newMin, max)

def generateID(rowNB, columnNB):
	return ((rowNB * 8) + columnNB)

with open('input.txt') as f:
    lines = f.readlines()

listOfID = []

for line in lines:
	row = (0, 127)
	column = (0, 7)
	for character in line:
		if (character == "F"):
			row = getLowerHalf(row)
		elif (character == "B"):
			row = getUpperHalf(row)
		elif (character == "L"):
			column = getLowerHalf(column)
		elif (character == "R"):
			column = getUpperHalf(column)

	result = generateID(row[0], column[0])
	listOfID.append(result)

highestValue = listOfID[0]

for ID in listOfID:
	if (ID > highestValue):
		highestValue = ID

print(highestValue)