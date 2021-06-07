with open('input.txt') as f:
    line = f.readline()

line = line.rstrip("\n")
actions = line.split(", ");
x_coordinate = 0
y_coordinate = 0
orientation = 0

visited_locations = []
find = False

for elem in actions:
	if elem[0] == "L":
		orientation -= 1
	elif elem[0] == "R":
		orientation += 1
	orientation = orientation % 4

	old_x_coordinate = x_coordinate
	old_y_coordinate = y_coordinate

	if (orientation == 0):
		y_coordinate += int(elem[1:])
	elif (orientation == 1):
		x_coordinate += int(elem[1:])
	elif (orientation == 2):
		y_coordinate -= int(elem[1:])
	elif (orientation == 3):
		x_coordinate -= int(elem[1:])

	new_visited_locations = []

	if (old_x_coordinate > x_coordinate):
		for x in range(old_x_coordinate, x_coordinate, -1):
			new_visited_locations.append([x, y_coordinate])
	elif (old_x_coordinate < x_coordinate):
		for x in range(old_x_coordinate, x_coordinate, 1):
			new_visited_locations.append([x, y_coordinate])
	if (old_y_coordinate > y_coordinate):
		for y in range(old_y_coordinate, y_coordinate, -1):
			new_visited_locations.append([x_coordinate, y])
	elif (old_y_coordinate < y_coordinate):
		for y in range(old_y_coordinate, y_coordinate, 1):
			new_visited_locations.append([x_coordinate, y])

	for elem in new_visited_locations:
		if (not elem in visited_locations):
			visited_locations.append(elem)
		else:
			print(abs(elem[0] + elem[1]))
			find = True
			break

	if (find):
		break