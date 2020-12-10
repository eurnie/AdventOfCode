import math

with open('input.txt') as f:
    lines = f.readlines()

total_value = 0

for elem in lines: 
	value = math.floor((int(elem) / 3) - 2)
	total_value += value

print(total_value)
