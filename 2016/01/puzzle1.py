with open('input.txt') as f:
    line = f.readline()

line = line.rstrip("\n")
actions = line.split(", ");
x_coordinate = 0
y_coordinate = 0
orientation = 0

for elem in actions:
	if elem[0] == "L":
		orientation -= 1
	elif elem[0] == "R":
		orientation += 1
	orientation = orientation % 4

	if (orientation == 0):
		y_coordinate += int(elem[1:])
	elif (orientation == 1):
		x_coordinate += int(elem[1:])
	elif (orientation == 2):
		y_coordinate -= int(elem[1:])
	elif (orientation == 3):
		x_coordinate -= int(elem[1:])

print(abs(x_coordinate + y_coordinate))