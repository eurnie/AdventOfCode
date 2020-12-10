with open('input.txt') as f:
    lines = f.readlines()

value1 = 0
value2 = 0
found = False

for line1 in lines:
	for line2 in lines:
		if ((int(line1) + int(line2)) == 2020):
			value1 = int(line1)
			value2 = int(line2)
			found = True
			break

	if (found):
		break

result = value1 * value2
print(result)
