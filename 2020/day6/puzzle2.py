def numberOfCharactersThatAppearXTimes(listOfCharacters, number):
	counter = 0
	dictOfCharacters = {char:listOfCharacters.count(char) for char in listOfCharacters}
	for elem in dictOfCharacters:
		if (dictOfCharacters[elem] == number):
			counter += 1
	return counter

with open('input.txt') as f:
    lines = f.readlines()

groupList = []
groupCounter = 0
counter = 0

for line in lines: 
	if (line == "\n"):
		counter += numberOfCharactersThatAppearXTimes(groupList, groupCounter)
		groupCounter = 0
		groupList = []
	else:
		groupCounter += 1
		for char in line:
			if (char != "\n"):
				groupList.append(char)

counter += numberOfCharactersThatAppearXTimes(groupList, groupCounter)

print(counter)