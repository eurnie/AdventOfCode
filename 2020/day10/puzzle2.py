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

# def createCheckList(inputList):
# 	checkList = []
# 	for x in range(0, len(inputList)):
# 		checkList.append([inputList[x], 0])
# 	return checkList
# 
# def nbOfOptions2(inputList, checkList):
# 	for number in reversed(inputList):
# 		index = inputList.index(number)
# 		if (index+1 < len(inputList)):
# 			if ((inputList[index+1] - inputList[index]) == 1) or ((inputList[index+1] - inputList[index]) == 3) or ((inputList[index+1] - inputList[index]) == 2):
# 				checkList[index+1][1] += 1
# 		if (index+2 < len(inputList)):
# 			if ((inputList[index+2] - inputList[index]) == 1) or ((inputList[index+2] - inputList[index]) == 3) or ((inputList[index+2] - inputList[index]) == 2):
# 				checkList[index+2][1] += 1
# 		if (index+3 < len(inputList)):
# 			if ((inputList[index+3] - inputList[index]) == 1) or ((inputList[index+3] - inputList[index]) == 3) or ((inputList[index+3] - inputList[index]) == 2):
# 				checkList[index+3][1] += 1
# 	checkList[0][1] = 1
# 	counter = 1
# 	for x in range(0, len(checkList)):
# 		if (checkList[x][1] > 1):
# 			counter *= checkList[x][1] - checkList[x-1][1] + 1
# 	return counter

# newList = createlistOfInput('input2.txt')
# print(nbOfOptions2(newList, createCheckList(newList)))

#######################################################

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

print(nbOfOptions(0, createlistOfInput('input1.txt')))