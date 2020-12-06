with open('input.txt') as f:
    lines = f.readlines()

groupList = []
counter = 0

for line in lines: 
	if (line == "\n"):
		counter += len(groupList)
		groupList = []
	else:
		for char in line:
			if ((char != "\n") and (not (char in groupList))):
				groupList.append(char)

counter += len(groupList)

print(counter)