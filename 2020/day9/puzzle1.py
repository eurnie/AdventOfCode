def createlistOfInput(input):
	with open(input) as f:
		lines = f.readlines()
	newList = []
	for line in lines:
		splitted = int(line[:-1])
		newList.append(splitted)
	return newList

def checkIfCorrectAddition(current, preamble, inputList):
	for x in range(current-preamble, current):
		for y in range(current-preamble, current):
			if (((inputList[x] + inputList[y]) == inputList[current]) and (x != y)):
				return checkIfCorrectAddition(current+1, preamble, inputList)
	return inputList[current]

print(checkIfCorrectAddition(25, 25, createlistOfInput('input.txt')))