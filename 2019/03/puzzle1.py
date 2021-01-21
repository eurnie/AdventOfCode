def calculateResult(input):
	with open(input) as f:
		lines = f.readlines()  	
	coordinatesWire1 = generateCoordinates(lines[0][:-1].split(','))
	coordinatesWire2 = generateCoordinates(lines[1][:-1].split(','))
	newlist = [ x for x in coordinatesWire1 if (x in coordinatesWire2)]
	return min(manhattanDistance(newlist))

def generateCoordinates(commands):
	current = (0,0)
	listOfCoordinates = []
	for elem in commands:
		direction = elem[0]
		size = int(elem[1:])
		if (direction == 'L'):
			for i in range(1, size+1):
				listOfCoordinates.append((current[0]-i, current[1]))
			current = (current[0]-size, current[1])
		elif (direction == 'R'):
			for i in range(1, size+1):
				listOfCoordinates.append((current[0]+i, current[1]))
			current = (current[0]+size, current[1])
		elif (direction == 'U'):
			for i in range(1, size+1):
				listOfCoordinates.append((current[0], current[1]+i))
			current = (current[0], current[1]+size)
		elif (direction == 'D'):
			for i in range(1, size+1):
				listOfCoordinates.append((current[0], current[1]-i))
			current = (current[0], current[1]-size)
	return listOfCoordinates
	
def manhattanDistance(coordinates):
	return [(abs(x[0]) + abs(x[1])) for x in coordinates]

print(calculateResult('input.txt'))