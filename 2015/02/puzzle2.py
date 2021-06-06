import copy

def lengthSmallestSides(list):
	smallest = list[0]
	for elem in list:
		if (elem < smallest):
			smallest = elem

	secondList = copy.deepcopy(list)
	secondList.remove(smallest)
	secondSmallest = secondList[0]
	for elem in secondList:
		if (elem < secondSmallest):
			secondSmallest = elem

	return (smallest+smallest+secondSmallest+secondSmallest)

lines = []

with open('input.txt') as f:
    lines = f.readlines()

total_surface = 0

for line in lines:
	line = line.rstrip("\n")
	dimension = line.split("x");
	dimension = list(map(int, dimension))
	l = dimension[0]
	w = dimension[1]
	h = dimension[2]
	surface_area = l*w*h
	surface_area += lengthSmallestSides(dimension)
	total_surface += surface_area


print(total_surface)