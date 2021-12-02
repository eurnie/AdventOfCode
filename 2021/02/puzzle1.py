with open('input.txt') as f:
    lines = f.readlines()

horizontal = 0
depth = 0

for line in lines:
	line_splitted = line.split(' ');
	if (line_splitted[0] == 'forward'):
		horizontal += int(line_splitted[1])

	if (line_splitted[0] == 'down'):
		depth += int(line_splitted[1])

	if (line_splitted[0] == 'up'):
		depth -= int(line_splitted[1])

print(horizontal * depth)