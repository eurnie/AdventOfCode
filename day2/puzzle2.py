def checkIfCorrectPassword(position1, position2, character, password):
	if ((password[position1] == character) and (password[position2] != character)):
		return True
	elif ((password[position1] != character) and (password[position2] == character)):
		return True
	else:
		return False

with open('input.txt') as f:
    lines = f.readlines()

number = 0 

for line in lines:
	list = line.split(" ")
	positionsSplitted = list[0].split("-")
	position1 = positionsSplitted[0]
	position2 = positionsSplitted[1]
	character = list[1][0]
	password = list[2]
	if checkIfCorrectPassword(int(position1)-1, int(position2)-1, character, password):
		number += 1

print(number)
