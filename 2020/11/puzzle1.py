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
			if (matrix[row][column] == 'L' and (nbOfAdjacentOccupied(row, column, matrix) == 0)):
				newMatrix[row][column] = '#'
	return newMatrix

def isEmptyPlace(character):
	if (character == '.') or (character == 'L'):
		return True
	return False

def deletePersons(matrix):
	newMatrix = copy.deepcopy(matrix)
	for row in range(0, len(matrix)):
		for column in range(0, len(matrix[row])):
			if (matrix[row][column] == '#' and (nbOfAdjacentOccupied(row, column, matrix) > 3)):
				newMatrix[row][column] = 'L'
	return newMatrix

def nbOfAdjacentOccupied(row, column, matrix):
	counter = 0
	if (row != 0) and (column != 0) and (not isEmptyPlace(matrix[row-1][column-1])):
		counter += 1
	if (row != 0) and (not isEmptyPlace(matrix[row-1][column])):
		counter += 1
	if (row != 0) and (column != len(matrix[0])-1) and (not isEmptyPlace(matrix[row-1][column+1])):
		counter += 1
	if (column != 0) and (not isEmptyPlace(matrix[row][column-1])):
		counter += 1
	if (column != len(matrix[0])-1) and (not isEmptyPlace(matrix[row][column+1])):
		counter += 1
	if (row != len(matrix)-1) and (column != 0) and (not isEmptyPlace(matrix[row+1][column-1])):
		counter += 1
	if (row != len(matrix)-1) and (not isEmptyPlace(matrix[row+1][column])):
		counter += 1
	if (row != len(matrix)-1) and (column != len(matrix[0])-1) and (not isEmptyPlace(matrix[row+1][column+1])):
		counter += 1
	return counter

def printMatrix(matrix):
	for row in matrix:
		printString = ''
		for elem in row:
			printString += elem
		print(printString)

print(createResult(createMatrix('input.txt')))