import copy

def createMatrix(input):
	with open(input) as f:
		lines = f.readlines()
	matrix = []
	for line in lines:
		newRow = []
		for character in line:
			if (character != '\n'):
				newRow.append(character)
		matrix.append(newRow)
	return matrix

def createResult(matrix):
	somethingChanged = True
	previousMatrix = matrix
	while somethingChanged:
		newMatrix = deletePersons(addPersons(previousMatrix))
		if (newMatrix == previousMatrix):
			somethingChanged = False
		previousMatrix = newMatrix
	return countNbOfOccupiedSeats(newMatrix)

def countNbOfOccupiedSeats(matrix):
	counter = 0
	for row in matrix:
		for elem in row:
			if (elem == '#'):
				counter += 1
	return counter

def addPersons(matrix):
	newMatrix = copy.deepcopy(matrix)
	for row in range(0, len(matrix)):
		for column in range(0, len(matrix[row])):
			if (matrix[row][column] == 'L' and (nbOfVisibleAdjacentOccupied(row, column, matrix) == 0)):
				newMatrix[row][column] = '#'
	return newMatrix

def deletePersons(matrix):
	newMatrix = copy.deepcopy(matrix)
	for row in range(0, len(matrix)):
		for column in range(0, len(matrix[row])):
			if (matrix[row][column] == '#' and (nbOfVisibleAdjacentOccupied(row, column, matrix) > 4)):
				newMatrix[row][column] = 'L'
	return newMatrix

def nbOfVisibleAdjacentOccupied(row, column, matrix):
	adjacent = [findUpper(row, column, matrix), findDown(row, column, matrix), findLeft(row, column, matrix), findRight(row, column, matrix), findUpperLeft(row, column, matrix), findUpperRight(row, column, matrix), findDownLeft(row, column, matrix), findDownRight(row, column, matrix)]
	counter = 0
	for elem in adjacent:
		if (elem == '#'):
			counter += 1
	return counter

def findUpper(row, column, matrix):
	place = '.'
	counter = 0
	while (place != 'L') and (place != '#'):
		counter -= 1
		if (not ((row+counter) < 0)):
			place = matrix[row+counter][column]
		else:
			break
	return place

def findDown(row, column, matrix):
	place = '.'
	counter = 0
	while (place != 'L') and (place != '#'):
		counter += 1
		if (not ((row+counter) >= len(matrix))):
			place = matrix[row+counter][column]
		else:
			break
	return place

def findLeft(row, column, matrix):
	place = '.'
	counter = 0
	while (place != 'L') and (place != '#'):
		counter -= 1
		if (not ((column+counter) < 0)):
			place = matrix[row][column+counter]
		else:
			break
	return place

def findRight(row, column, matrix):
	place = '.'
	counter = 0
	while (place != 'L') and (place != '#'):
		counter += 1
		if (not ((column+counter) >= len(matrix[row]))):
			place = matrix[row][column+counter]
		else:
			break
	return place

def findUpperRight(row, column, matrix):
	place = '.'
	counter1 = 0
	counter2 = 0
	while (place != 'L') and (place != '#'):
		counter1 -= 1
		counter2 += 1
		if (not ((row+counter1) < 0)) and (not ((column+counter2) >= len(matrix[0]))):
			place = matrix[row+counter1][column+counter2]
		else:
			break
	return place

def findUpperLeft(row, column, matrix):
	place = '.'
	counter1 = 0
	counter2 = 0
	while (place != 'L') and (place != '#'):
		counter1 -= 1
		counter2 -= 1
		if (not ((row+counter1) < 0)) and (not ((column+counter2) < 0)):
			place = matrix[row+counter1][column+counter2]
		else:
			break
	return place

def findDownRight(row, column, matrix):
	place = '.'
	counter1 = 0
	counter2 = 0
	while (place != 'L') and (place != '#'):
		counter1 += 1
		counter2 += 1
		if (not ((row+counter1) >= len(matrix))) and (not ((column+counter2) >= len(matrix[0]))):
			place = matrix[row+counter1][column+counter2]
		else:
			break
	return place

def findDownLeft(row, column, matrix):
	place = '.'
	counter1 = 0
	counter2 = 0
	while (place != 'L') and (place != '#'):
		counter1 += 1
		counter2 -= 1
		if (not ((row+counter1) >= len(matrix))) and (not ((column+counter2) < 0)):
			place = matrix[row+counter1][column+counter2]
		else:
			break
	return place

def printMatrix(matrix):
	for row in matrix:
		printString = ''
		for elem in row:
			printString += elem
		print(printString)

print(createResult(createMatrix('input.txt')))