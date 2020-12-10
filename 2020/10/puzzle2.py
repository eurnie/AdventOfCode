def createlistOfInput(input):
	with open(input) as f:
		lines = f.readlines()
	newList = [0]
	for line in lines:
		splitted = int(line[:-1])
		newList.append(splitted)
	newList.sort()
	newList.append(newList[len(newList)-1]+3)
	return newList

def createCheckList(inputList):
	checkList = []
	for x in range(0, len(inputList)):
		checkList.append([inputList[x], 0])
	for number in reversed(inputList):
		index = inputList.index(number)
		if (index+1 < len(inputList)) and (reachable(inputList[index], inputList[index+1])):
				checkList[index+1][1] += 1
		if (index+2 < len(inputList)) and (reachable(inputList[index], inputList[index+2])):
				checkList[index+2][1] += 1
		if (index+3 < len(inputList)) and (reachable(inputList[index], inputList[index+3])):
				checkList[index+3][1] += 1
	checkList[0][1] = 1
	return checkList

def calculateResult(inputList):
	checkList = createCheckList(inputList)
	for x in range(0, len(checkList)):
		if ((x-1 > 0) and reachable(checkList[x-1][0], checkList[x][0])):
			checkList[x][1] += checkList[x-1][1] -1
		if ((x-2 > 0) and reachable(checkList[x-2][0], checkList[x][0])):
			checkList[x][1] += checkList[x-2][1] -1
		if ((x-3 > 0) and reachable(checkList[x-3][0], checkList[x][0])):
			checkList[x][1] += checkList[x-3][1] -1
	return checkList[len(checkList)-1][1]

def reachable(number1, number2):
	return ((number2 - number1) <= 3)

print(calculateResult(createlistOfInput('input.txt')))

#######################################################

# this is another solution that is less efficient
def nbOfOptions(current, inputList):
	if (current == (len(inputList)-1)):
		return 1
	total = 0
	if (current+1 < len(inputList)):
		if ((inputList[current+1] - inputList[current]) == 1) or ((inputList[current+1] - inputList[current]) == 3) or ((inputList[current+1] - inputList[current]) == 2):
			total +=  nbOfOptions(current+1, inputList)
	if (current+2 < len(inputList)):
		if ((inputList[current+2] - inputList[current]) == 1) or ((inputList[current+2] - inputList[current]) == 3) or ((inputList[current+2] - inputList[current]) == 2):
			total +=  nbOfOptions(current+2, inputList)
	if (current+3 < len(inputList)):
		if ((inputList[current+3] - inputList[current]) == 1) or ((inputList[current+3] - inputList[current]) == 3) or ((inputList[current+3] - inputList[current]) == 2):
			total +=  nbOfOptions(current+3, inputList)
	return total

# print(nbOfOptions(0, createlistOfInput('input2.txt')))