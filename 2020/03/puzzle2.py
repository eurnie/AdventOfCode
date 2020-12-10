def getNumberOfTrees(right, down):
	with open('input.txt') as f:
		lines = f.readlines()

	counter = 0
	numberOfTrees = 0

	for i in range(0, len(lines), down):
		line = lines[i]
		if (line[counter] == "#"):
			numberOfTrees += 1
		counter = (counter + right) % (len(line) - 1)

	return numberOfTrees

result = getNumberOfTrees(1, 1) * getNumberOfTrees(3, 1) * getNumberOfTrees(5, 1) * getNumberOfTrees(7, 1) * getNumberOfTrees(1, 2)
print(result)
