def countNumberOfCharacters(character, password):
	number = 0
	for char in password:
		if (char == character):
			number += 1
	return number

def checkIfCorrectPassword(min, max, character, password):
	number = countNumberOfCharacters(character, password)
	if ((number >= min) and (number <= max)):
		return True
	else:
		return False

with open('input.txt') as f:
    lines = f.readlines()

number = 0 

for line in lines:
	list = line.split(" ")
	minAndMaxSplitted = list[0].split("-")
	min = minAndMaxSplitted[0]
	max = minAndMaxSplitted[1]
	character = list[1][0]
	password = list[2]
	if checkIfCorrectPassword(int(min), int(max), character, password):
		number += 1

print(number)
