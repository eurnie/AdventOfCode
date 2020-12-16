with open('input.txt') as f:
	lines = f.readlines()

timestamp = int(lines[0])
busses = []

for character in lines[1].split(','):
	if (character != 'x') and (character != '\n'):
		busses.append(int(character))

smallestDifference = 10000000
smallestDifferenceBus = 1

for bus in busses:
	counter = bus
	while (counter < timestamp):
		counter += bus
	if ((counter - timestamp) < smallestDifference):
		smallestDifference = counter - timestamp
		smallestDifferenceBus = bus

print(smallestDifferenceBus * smallestDifference)