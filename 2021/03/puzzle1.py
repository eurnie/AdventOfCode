with open('input.txt') as f:
    lines = f.readlines()

gamma = ""
epsilon = ""

for i in range(0, len(lines[0])-1):
    nb_of_zeros = 0
    nb_of_ones = 0

    for line in lines:
        if line[i] == "0":
            nb_of_zeros += 1
        if line[i] == "1":
            nb_of_ones += 1

    if (nb_of_zeros > nb_of_ones):
        gamma += "0"
        epsilon += "1"
    elif (nb_of_ones > nb_of_zeros):
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))