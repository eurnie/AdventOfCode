def createDictionary(file):
	with open(file) as f:
		lines = f.readlines()
	dictionary = {}
	for line in lines:
		cleanLine = line[:-2]
		splitContain = cleanLine.split('contain')
		splitComma = splitContain[1][1:].split(', ')
		stringList = []
		for string in splitComma:
			splitSpace = string.split(' ')
			number = splitSpace[0]
			if (splitSpace[0] == 'no'):
				correctString = 'none'
				number = 0
			else:
				correctString = splitSpace[1] + " " + splitSpace[2]
			correctTuple = (correctString, number)
			stringList.append(correctTuple)
		dictionary[splitContain[0][:-6]] = stringList
	return dictionary

def numberOfBagsNeeded(elem, dictionary):
	counter = 0
	for subBag in dictionary[elem]:
		if (subBag[0] != 'none'):
			counter += int(subBag[1]) + (int(subBag[1]) * numberOfBagsNeeded(subBag[0], dictionary))
	return counter

print(numberOfBagsNeeded("shiny gold", dictionary = createDictionary('input.txt')))