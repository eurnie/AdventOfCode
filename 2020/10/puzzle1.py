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

def calculateResult(inputList):
	numberOf1 = 0
	numberOf3 = 0
	for x in range(1, len(inputList)):
		if ((inputList[x] - inputList[x-1]) == 1):
			numberOf1 += 1
		elif ((inputList[x] - inputList[x-1]) == 3):
			numberOf3 += 1
	return (numberOf1 * numberOf3)

print(calculateResult(createlistOfInput('input.txt')))