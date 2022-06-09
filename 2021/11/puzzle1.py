import copy

def create_matrix(input):
    with open(input) as f:
        lines = f.readlines()

    matrix = []

    for line in lines: 
        new_row = []
        for elem in line:
            if (elem != '\n'):
                new_row.append(int(elem))
        matrix.append(new_row)

    return matrix

def count_nb_flashes(matrix):
    count = 0
    for row in matrix:
        for element in row:
            count += element
    return count

def simulate_step(old_matrix):
    matrix = copy.deepcopy(old_matrix)
    has_flashed = copy.deepcopy(old_matrix)

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            matrix[y][x] += 1
            has_flashed[y][x] = 0

    old_count = 1
    while (old_count != count_nb_flashes(has_flashed)):
        old_count = count_nb_flashes(has_flashed)
        for y in range(0, len(matrix)):
            for x in range(0, len(matrix[y])):
                if (matrix[y][x] > 9) and (has_flashed[y][x] == 0):
                    has_flashed[y][x] = 1
                    if (x-1) >= 0:
                        matrix[y][x-1] += 1
                    if (x+1) < len(matrix[y]):
                        matrix[y][x+1] += 1
                    if (y-1) >= 0:
                        matrix[y-1][x] += 1
                    if (y+1) < len(matrix):
                        matrix[y+1][x] += 1
                    if ((x-1) >= 0) and ((y-1) >= 0):
                        matrix[y-1][x-1] += 1
                    if ((x+1) < len(matrix[y])) and ((y-1) >= 0):
                        matrix[y-1][x+1] += 1
                    if ((x-1) >= 0) and ((y+1) < len(matrix)):
                        matrix[y+1][x-1] += 1
                    if ((x+1) < len(matrix[y])) and ((y+1) < len(matrix)):
                        matrix[y+1][x+1] += 1

    for y in range(0, len(matrix)):
        for x in range(0, len(matrix[y])):
            if (has_flashed[y][x] == 1):
                matrix[y][x] = 0

    return matrix, count_nb_flashes(has_flashed)

def total_flashes_after_x_steps(x, input):
    count = 0
    matrix = create_matrix(input)

    for _ in range(x):
        matrix, nb_flashes = simulate_step(matrix)
        count += nb_flashes

    return count

print(total_flashes_after_x_steps(100, 'input.txt'))