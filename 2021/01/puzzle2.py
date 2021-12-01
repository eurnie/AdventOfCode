with open('input.txt') as f:
    lines = f.readlines()

nb_of_increasements = 0
previous_value = 0

for i in range(0, len(lines)-2):
	current_value = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
	if ((previous_value != 0) and (current_value > previous_value)):
		nb_of_increasements += 1
	previous_value = current_value

print(nb_of_increasements)