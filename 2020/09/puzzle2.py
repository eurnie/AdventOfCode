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

def findContiguousSet(number, inputList):
	for x in range(0, len(inputList)):
		sum = inputList[x]
		counter = 0
		while (sum < number):
			counter += 1
			sum += inputList[x + counter]
			if (sum == number):
				return inputList[x:x+counter]

def calculateResult(inputList):
	return min(inputList) + max(inputList)

inputList = createlistOfInput('input.txt')
print(calculateResult(findContiguousSet(checkIfCorrectAddition(25, 25, inputList), inputList)))