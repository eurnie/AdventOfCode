with open('input.txt') as f:
    line = f.readline()

count_left_open = 0
count_right_open = 0

for elem in line:
	if elem == ")":
		count_left_open += 1
	elif elem == "(":
		count_right_open += 1

print(count_right_open - count_left_open)