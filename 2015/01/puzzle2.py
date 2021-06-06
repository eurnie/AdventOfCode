with open('input.txt') as f:
    line = f.readline()

floor = 0
counter = 0

for elem in line:
	counter += 1
	if elem == ")":
		floor -= 1
	elif elem == "(":
		floor += 1

	if (floor == -1):
		print(counter)
		break