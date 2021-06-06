def find_largest(list):
	largest = list[0]
	for elem in list:
		if elem > largest:
			largest = elem
	return largest

def find_smallest(list):
	smallest = list[0]
	for elem in list:
		if elem < smallest:
			smallest = elem
	return smallest

lines = []

with open('input.txt') as f:
    lines = f.readlines()

checksum = 0

for line in lines:
	line = line.rstrip("\n")
	numbers = line.split("\t")
	numbers = list(map(int, numbers))
	checksum += find_largest(numbers) - find_smallest(numbers)

print(checksum)