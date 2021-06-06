def smallestArea(list):
	smallest = list[0]
	for elem in list:
		if (elem < smallest):
			smallest = elem
	return smallest

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
	surface_area = (2*l*w)+(2*w*h)+(2*h*l)
	surface_area += smallestArea([l*w, w*h, h*l])
	total_surface += surface_area


print(total_surface)