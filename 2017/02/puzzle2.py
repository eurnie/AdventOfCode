def find_evenly_divide(list):
	for elem1 in list:
		for elem2 in list:
			if (int(elem1) != int(elem2)):
				if ((int(elem1) % int(elem2)) == 0):
					return round((int(elem1) / int(elem2)))
	return 0

lines = []

with open('input.txt') as f:
    lines = f.readlines()

checksum = 0

for line in lines:
	line = line.rstrip("\n")
	numbers = line.split("\t")
	numbers = list(map(int, numbers))
	checksum += find_evenly_divide(numbers)

print(checksum)