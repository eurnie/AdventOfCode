with open('input.txt') as f:
	lines = f.readlines()

waypoint = [10, 1]
position = [0, 0]

for line in lines:
	command = line[0]
	value = int(line[1:])
	if (command == 'N'):
		waypoint[1] += value
	elif (command == 'S'):
		waypoint[1] -= value
	elif (command == 'E'):
		waypoint[0] += value
	elif (command == 'W'):
		waypoint[0] -= value
	elif (command == 'L'):
		timesL = int(value / 90)
		for i in range(0, timesL):
			newX = -1 * waypoint[1]
			newY = waypoint[0]
			waypoint = [newX, newY]
	elif (command == 'R'):
		timesR = int(value / 90)
		for i in range(0, timesR):
			newX = waypoint[1]
			newY = -1 * waypoint[0]
			waypoint = [newX, newY]
	elif (command == 'F'):
		for i in range(0, value):
			position[0] += waypoint[0]
			position[1] += waypoint[1]

print(abs(position[0]) + abs(position[1]))