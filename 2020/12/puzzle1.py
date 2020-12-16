with open('input.txt') as f:
	lines = f.readlines()

position = [0, 0]
facing = 0

for line in lines:
	command = line[0]
	value = int(line[1:])
	if (command == 'N'):
		position[1] += value
	elif (command == 'S'):
		position[1] -= value
	elif (command == 'E'):
		position[0] += value
	elif (command == 'W'):
		position[0] -= value
	elif (command == 'L'):
		facing = (facing + value) % 360
	elif (command == 'R'):
		facing = (facing - value) % 360
		while (facing < 0):
			facing = (facing + 360) % 360
	elif (command == 'F'):
		if (facing == 0):
			position[0] += value
		elif (facing == 90):
			position[1] += value
		elif (facing == 180):
			position[0] -= value
		elif (facing == 270):
			position[1] -= value

print(abs(position[0]) + abs(position[1]))