with open('input.txt') as f:
    lines = f.readlines()

counter = 0
numberOfTrees = 0

for line in lines:
	if (line[counter] == "#"):
		numberOfTrees += 1
	counter = (counter + 3) % (len(line) - 1)

print(numberOfTrees)
