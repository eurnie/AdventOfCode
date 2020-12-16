import copy

listOfRules = []
listOfTickets = []
listOfClasses = []
ownTicket = []

def createListOfRulesAndListOfTickets(input):
	with open(input) as f:
		lines = f.readlines()
	rules = True
	tickets = False
	myTicket = False
	for line in lines:
		if (line != '\n') and (rules):
			# add new rule
			ruleName = line[:-1].split(':')[0]
			splitted = line[:-1].split(':')[1]
			splitted2 = splitted[1:].split(' or ')
			for elem in splitted2:
				splitted3 = elem.split('-')
				listOfNumbers = [int(splitted3[0]), int(splitted3[1]), ruleName]
				listOfRules.append(listOfNumbers)
		elif (tickets):
			# add new ticket
			newList = []
			splittedLine = line.split(',')
			for elem in splittedLine:
				if (elem != '\n'):
					newList.append(int(elem))
			listOfTickets.append(newList)
		elif (myTicket):
			splittedLine = line.split(',')
			for elem in splittedLine:
				if (elem != '\n'):
					ownTicket.append(int(elem))
			myTicket = False
		else:
			if ('your ticket:' in line):
				myTicket = True
			if ('nearby tickets:' in line):
				tickets = True
			rules = False
	deleteFalseTickets()
	listToAdd = []
	for rule in listOfRules:
		if (not (rule[2] in listToAdd)):
			listToAdd.append(rule[2])
	for i in range(0, len(listOfTickets[0])):
		listOfClasses.append(copy.deepcopy(listToAdd))

def deleteFalseTickets():
	errorList = []
	for ticket in listOfTickets:
		for ticketNumber in ticket:
			if (not legalNumber(ticketNumber)):
				errorList.append(ticket)
	for errorTicket in errorList:
		listOfTickets.remove(errorTicket)

def legalNumber(number):
	result = False
	for rule in listOfRules:
		if (number >= rule[0]) and (number <= rule[1]):
			result = True
			break
	return result

def determineClasses():
	for ticket in listOfTickets:
		for number in ticket:
			ticketClasses = listOfClasses[ticket.index(number)]	
			classes = toWichClassesBelong(number)
			toRemove = []
			for element in ticketClasses:
				if (not (element in classes)):
					toRemove.append(element)
			for removeElement in toRemove:
				ticketClasses.remove(removeElement)
	deleteDecidedElements(0)

def toWichClassesBelong(number):
	returnList = []
	for rule in listOfRules:
		if (number >= rule[0]) and (number <= rule[1]):
			returnList.append(rule[2])
	return returnList

def deleteDecidedElements(previous):
	decided = []
	for classEntry in listOfClasses:
		if (len(classEntry) == 1):
			decided.append(classEntry[0])
	for decidedelement in decided:
		for classEntry2 in listOfClasses: 
			if (len(classEntry2) != 1):
				if (decidedelement in classEntry2):
					classEntry2.remove(decidedelement)
	if (len(decided) > previous):
		deleteDecidedElements(len(decided))

def createResult():
	determineClasses()
	listWithIndices = getIndicesWithDeparture()
	result = 1
	for index in listWithIndices:
		result *= ownTicket[index]
	return result

def getIndicesWithDeparture():
	returnList = []
	for element in listOfClasses:
		if ('departure' in element[0]):
			returnList.append(listOfClasses.index(element))
	return returnList

createListOfRulesAndListOfTickets('input.txt')
print(createResult())