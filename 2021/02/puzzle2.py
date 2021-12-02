with open('input.txt') as f:
    lines = f.readlines()

horizontal = 0
depth = 0
aim = 0

for line in lines:
    line_splitted = line.split(' ');
    if (line_splitted[0] == 'forward'):
        horizontal += int(line_splitted[1])
        depth += aim * int(line_splitted[1])

    if (line_splitted[0] == 'down'):
        aim += int(line_splitted[1])

    if (line_splitted[0] == 'up'):
        aim -= int(line_splitted[1])

print(horizontal * depth)