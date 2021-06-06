with open('input.txt') as f:
    line = f.readline()

line = line.rstrip("\n")

count = 0

for x in range(0, len(line)):
	size = len(line)
	other_index = round((x + (size/2)) % (size))

	if (line[x] == line[other_index]):
		count += int(line[x])

print(count)