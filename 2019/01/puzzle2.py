import math

def calculate_fuel(number):
	if (number > 0):
		total_fuel_needed = 0
		fuel_needed = math.floor((number / 3) - 2)
		if (fuel_needed > 0):
			total_fuel_needed += fuel_needed
			total_fuel_needed += calculate_fuel(fuel_needed)
		return int(total_fuel_needed)
	else:
		return 0

with open('input.txt') as f:
    lines = f.readlines()

total_value = 0

for elem in lines:
	value = calculate_fuel(int(elem))
	total_value += value

print(total_value)
