def check_if_low_point(x, y, matrix):
    if (y-1 > -1) and (y-1 < len(matrix[x])):
        top = matrix[x][y-1]
    else:
        top = 9

    if (y+1 > -1) and (y+1 < len(matrix[x])):
        down = matrix[x][y+1]
    else:
        down = 9

    if (x-1 > -1) and (x-1 < len(matrix)):
        left = matrix[x-1][y]
    else:
        left = 9

    if (x+1 > -1) and (x+1 < len(matrix)):
        right = matrix[x+1][y]
    else:
        right = 9
    
    to_compare = matrix[x][y]

    if (to_compare < top) and (to_compare < down) and (to_compare < left) and (to_compare < right):
        return True 
    else:
        return False

with open("input.txt") as f:
    lines = f.readlines()

matrix = []

for line in lines:
    new_row = []
    for char in line:
        if (char != '\n'):
            new_row.append(int(char))
    matrix.append(new_row)

total_count = 0

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if check_if_low_point(x, y, matrix):
            total_count += matrix[x][y] + 1

print(total_count)