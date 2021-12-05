def drawVerticalLine(matrix, x, y1, y2):
    if (y2 > y1):
        for i in range(y1, y2+1):
            matrix[i][x] += 1
    else:
        for i in range(y2, y1+1):
            matrix[i][x] += 1

def drawHorizontalLine(matrix, y, x1, x2):
    if (x2 > x1):
        for i in range(x1, x2+1):
            matrix[y][i] += 1
    else:
        for i in range(x2, x1+1):
            matrix[y][i] += 1

def drawDiagonalLine(matrix, x1, x2, y1, y2):
    coordinateX = x1
    coordinateY = y1
    matrix[coordinateY][coordinateX] += 1

    while (coordinateX != x2) and (coordinateY != y2):
        if ((x1 > x2) and (y2 > y1)):
            coordinateX -= 1
            coordinateY += 1
        elif ((x1 > x2) and (y2 < y1)):
            coordinateX -= 1
            coordinateY -= 1
        elif ((x2 > x1) and (y1 < y2)):
            coordinateX += 1
            coordinateY += 1
        elif ((x1 < x2) and (y2 < y1)):
            coordinateX += 1
            coordinateY -= 1
        matrix[coordinateY][coordinateX] += 1

with open("input.txt") as f:
    lines = f.readlines()

matrix = []
for i in range(0, 1000):
    row = []
    for j in range(0, 1000):
        row.append(0)
    matrix.append(row)

for line in lines:
    coordinates = line.split(" -> ")
    x1 = int(coordinates[0].split(",")[0])
    y1 = int(coordinates[0].split(",")[1])
    x2 = int(coordinates[1].split(",")[0])
    y2 = int(coordinates[1].split(",")[1])
    if (x1 == x2):
        drawVerticalLine(matrix, x1, y1, y2)
    elif (y1 == y2):
        drawHorizontalLine(matrix, y1, x1, x2)
    else:
        drawDiagonalLine(matrix, x1, x2, y1, y2)

count = 0
for row in matrix:
    for element in row:
        if (element > 1):
            count += 1

print(count)