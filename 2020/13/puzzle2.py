with open('input.txt') as f:
	lines = f.readlines()

busses = []
counter = 0

for character in lines[1].split(','):
	if (character != '\n'):
		if (character != 'x'):
			busses.append((int(character), counter))
		counter += 1

highestBus = busses[0][0]
highestBusOffset = busses[0][1]
for bus in busses:
	if (bus[0] > highestBus):
		highestBus = bus[0]
		highestBusOffset = bus[1]

# 5263308589737
number = highestBus - highestBusOffset
found = False

while (not found):
	number2 = 0
	for bus in busses:
		if (((number+bus[1]) % bus[0]) == 0):
			number2 += 1
		else:
			break
	if (number2 == len(busses)):
		found = True
		break
	number += highestBus

print(number)