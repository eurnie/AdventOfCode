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

def calculateResult(image):
	bestLayer = image[0]
	bestLayerScore = nbOfDigits(bestLayer, '0')
	for layer in image:
		if (nbOfDigits(layer, '0') < bestLayerScore):
			bestLayer = layer
			bestLayerScore = nbOfDigits(layer, '0')
	nbOfOne = nbOfDigits(bestLayer, '1')
	nbOfTwo = nbOfDigits(bestLayer, '2')
	return (nbOfOne * nbOfTwo)

def nbOfDigits(layer, nb):
	counter = 0
	for row in layer:
		for number in row:
			if (number == nb):
				counter += 1
	return counter

print(calculateResult(createImage('input.txt')))