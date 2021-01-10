import copy

def createImage(input):
	with open(input) as f:
		firstLine = f.readline()

	width = 25
	tall = 6
	image = []
	row = []
	layer = []

	for number in firstLine:
		if (len(row) < width):
			row.append(number)
		else:
			layer.append(copy.deepcopy(row))
			row = []
			row.append(number)
			if (len(layer) == tall):
				image.append(copy.deepcopy(layer))
				layer = []
	return image

def renderImage(image):
	newImage = []
	for i in range(0, len(image[0])):
		newRow = []
		for j in range(0, len(image[0][0])):
			counter = 0
			while (image[counter][i][j] == '2'):
				counter += 1
			newRow.append(image[counter][i][j])
		newImage.append(copy.deepcopy(newRow))
	return newImage

def printImage(image):
	for row in image:
		for number in row:
			if (number == '0'):
				print(' ', end="")
			elif (number == '1'):
				print('#', end="")
		print('')

printImage(renderImage(createImage('input.txt')))