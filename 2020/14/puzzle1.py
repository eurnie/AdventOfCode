def execute(input):
	mask = ['X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X','X']
	memory = {}

	with open(input) as f:
		lines = f.readlines()

	for line in lines:
		if ('mask' in line):
			splittedLine = line.split('= ')
			for x in range(0, len(splittedLine[1][:-1])):
				mask[x] = splittedLine[1][:-1][x]
		elif ('mem' in line):
			splittedLine = line.split('[')
			position = splittedLine[1].split(']')[0]
			splittedLine2 = splittedLine[1].split('= ')
			value = splittedLine2[1][:-1]
			newValue = calculateMemoryValue(toBinaryList(int(value)), mask)
			memory[position] = newValue

	return calculateResult(memory)

def calculateMemoryValue(binaryList, mask):
	newBinaryList = []
	for i in range(0, len(mask)):
		if (mask[i] == 'X'):
			newBinaryList.append(binaryList[i])
		elif (mask[i] == '0'):
			newBinaryList.append(0)
		elif (mask[i] == '1'):
			newBinaryList.append(1)
	return toNumber(newBinaryList)

def toBinaryList(number):
	temp = number
	binaryList = []
	for i in range(35, -1, -1): 
		if (temp >= (2 ** i)):
			binaryList.append(1)
			temp -= 2 ** i
		else:
			binaryList.append(0)
	return binaryList

def toNumber(binaryList):
	counter = 0
	for i in range(0, len(binaryList)):
		counter += binaryList[len(binaryList)-i-1] * (2 ** i)
	return counter

def calculateResult(memory):
	counter = 0
	for key in memory:
		counter += int(memory[key])
	return counter

print(execute('input.txt'))