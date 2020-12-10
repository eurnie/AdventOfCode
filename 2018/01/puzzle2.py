lines = []
list_frequencies = [0]

with open('input.txt') as f:
    lines = f.readlines()

current = 0
found = False

while (found == False):
	for line in lines:
		current += int(line)
		if (current in list_frequencies):
			print(current)
			found = True
			break
		else:
			list_frequencies.append(current)
