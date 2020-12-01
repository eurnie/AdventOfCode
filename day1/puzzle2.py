with open('input.txt') as f:
    lines = f.readlines()

value1 = 0
value2 = 0
value3 = 0
found = False

for line1 in lines:
	for line2 in lines:
		for line3 in lines:
			if ((int(line1) + int(line2) + int(line3)) == 2020):
				value1 = int(line1)
				value2 = int(line2)
				value3 = int(line3)
				found = True
				break

		if (found):
			break
	if (found):
		break

result = value1 * value2 * value3
print(result)
