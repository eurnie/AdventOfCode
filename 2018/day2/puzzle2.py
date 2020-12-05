def createResult(line1, line2):
	result = ""
	for x in range(0, len(line1) - 1):
		if (line1[x] == line2[x]):
			result += line1[x]
	print(result)

with open('input.txt') as f:
    lines = f.readlines()

found = False

for line1 in lines:
	for line2 in lines:
		if ( (line1 != line2) and (not found)):
			number_of_differences = 0
			for x in range(0, len(line1) - 1):
				if (line1[x] != line2[x]):
					number_of_differences += 1
			if (number_of_differences == 1):
				createResult(line1, line2)
				found = True
				break
