with open('input.txt') as f:
    line = f.readline()

line = line.rstrip("\n")

count = 0

for x in range(0, len(line)+1):
	if ( (x < len(line)-1) and (line[x] == line[x+1]) ):
		count += int(line[x])
	elif ( (x == len(line)-1) and (line[x] == line[0]) ):
		count += int(line[x])

print(count)