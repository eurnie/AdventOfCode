listOfRules = []
listOfTickets = []

def createListOfRulesAndListOfTickets(input):
	with open(input) as f:
		lines = f.readlines()
	rules = True
	tickets = False
	for line in lines:
		if (line != '\n') and (rules):
			# add new rule
			splitted = line[:-1].split(':')[1]
			splitted2 = splitted[1:].split(' or ')
			for elem in splitted2:
				splitted3 = elem.split('-')
				listOfNumbers = [int(splitted3[0]), int(splitted3[1])]
				listOfRules.append(listOfNumbers)
		elif (tickets):
			# add new ticket
			newList = []
			splittedLine = line.split(',')
			for elem in splittedLine:
				if (elem != '\n'):
					newList.append(int(elem))
			listOfTickets.append(newList)
		else:
			if ('nearby tickets:' in line):
				tickets = True
			rules = False

def createResult():
	errorList = []
	for ticket in listOfTickets:
		for ticketNumber in ticket:
			if (not legalNumber(ticketNumber)):
				errorList.append(ticketNumber)
	value = 0
	for errorNumber in errorList:
		value += errorNumber
	return value

def legalNumber(number):
	result = False
	for rule in listOfRules:
		if (number >= rule[0]) and (number <= rule[1]):
			result = True
			break
	return result

createListOfRulesAndListOfTickets('input.txt')
print(createResult())