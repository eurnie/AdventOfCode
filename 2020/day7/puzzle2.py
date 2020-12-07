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
			if (splitSpace[0] == 'no'):
				correctString = 'none'
			else:
				correctString = splitSpace[1] + " " + splitSpace[2]
			stringList.append(correctString)
		dictionary[splitContain[0][:-6]] = stringList
	return dictionary

def printDictionary(dictionary):
	for elem in dictionary:
		print(elem, "  :  ", dictionary[elem])

def numberOfBagsThatCanHoldAnInstance(dictionary, bag):
	counter = 0
	for elem in dictionary:
		if (elemCanHoldBag(elem, dictionary, bag)):
			counter +=1
	return counter

def elemCanHoldBag(elem, dictionary, bag):
	listOfBooleans = []
	listOfCandidates = dictionary[elem]
	if (bag in listOfCandidates):
		return True
	for candidate in listOfCandidates:
		if (candidate == 'none'):
			listOfBooleans.append(False)
		else:
			listOfBooleans.append(elemCanHoldBag(candidate, dictionary, bag))
	returnValue = False
	for element in listOfBooleans:
		returnValue = returnValue or element
	return returnValue

dictionary = createDictionary('input.txt')
printDictionary(dictionary)
print(numberOfBagsThatCanHoldAnInstance(dictionary, "shiny gold"))