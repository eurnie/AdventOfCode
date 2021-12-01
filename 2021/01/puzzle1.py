with open('input.txt') as f:
    lines = f.readlines()

nb_of_increasements = 0
previous_value = 0

for line in lines:
	if ((previous_value != 0) and (int(line) > previous_value)):
		nb_of_increasements += 1
	previous_value = int(line)

print(nb_of_increasements)