def checkIfCorrectBYR(input):
	if ((int(input) >= 1920) and (int(input) <= 2002)):
		return True
	return False

def checkIfCorrectIYR(input):
	if ((int(input) >= 2010) and (int(input) <= 2020)):
		return True
	return False

def checkIfCorrectEYR(input):
	if ((int(input) >= 2020) and (int(input) <= 2030)):
		return True
	return False

def checkIfCorrectHGT(input):
	lastCharacter = input[-1]
	if (lastCharacter == "\n"):
		input = input[:-1]
	unit = input[-2:]
	value = input[:-2]
	if (unit == "cm"):	
		if ((int(value) >= 150) and (int(value) <= 193)):
			return True
	elif (unit == "in"):
		if ((int(value) >= 59) and (int(value) <= 76)):
			return True
	return False

def checkIfCorrectHCL(input):
	lastCharacter = input[-1]
	if (lastCharacter == "\n"):
		input = input[:-1]
	if (len(input) == 7):
		if (input[0] == "#"):
			counter = 1
			check = True
			while ((counter < len(input)) and (check)):
				str = input[counter]
				check = False
				if ((str.isdigit()) or (legalHCLCharacter(str))):
					check = True
				counter += 1
			if (check):
				return True

	return False

def legalHCLCharacter(input):
	if (input == "a"):
		return True
	elif (input == "b"):
		return True
	elif (input == "b"):
		return True
	elif (input == "c"):
		return True
	elif (input == "d"):
		return True
	elif (input == "e"):
		return True
	elif (input == "f"):
		return True
	return False

def checkIfCorrectECL(input):
	lastCharacter = input[-1]
	if (lastCharacter == "\n"):
		input = input[:-1]
	if (input == "amb"):
		return True
	elif (input == "blu"):
		return True
	elif (input == "brn"):
		return True
	elif (input == "gry"):
		return True
	elif (input == "grn"):
		return True
	elif (input == "hzl"):
		return True
	elif (input == "oth"):
		return True
	return False

def checkIfCorrectPID(input):
	lastCharacter = input[-1]
	if (lastCharacter == "\n"):
		input = input[:-1]
	if ((len(input) == 9) and (input.isdigit())):
		return True
	return False

with open('input.txt') as f:
    lines = f.readlines()

# list = [byr, iyr, eyr, hgt, hcl, ecl, pid, cid]
list = [False, False, False, False, False, False, False, False]
counter = 0

for line in lines:
	if (line == '\n'):
		if ( (list == [True, True, True, True, True, True, True, False]) or ((list == [True, True, True, True, True, True, True, True])) ):
			counter += 1
		list = [False, False, False, False, False, False, False, False]
	else:
		line1 = line.split(" ")
		for elem in line1:
			elem1 = elem.split(":")
			if (elem1[0] == "byr"):
				if (checkIfCorrectBYR(elem1[1])):
					list[0] = True
			elif (elem1[0] == "iyr"):
				if (checkIfCorrectIYR(elem1[1])):
					list[1] = True
			elif (elem1[0] == "eyr"):
				if (checkIfCorrectEYR(elem1[1])):
					list[2] = True
			elif (elem1[0] == "hgt"):
				if (checkIfCorrectHGT(elem1[1])):
					list[3] = True
			elif (elem1[0] == "hcl"):
				if (checkIfCorrectHCL(elem1[1])):
					list[4] = True
			elif (elem1[0] == "ecl"):
				if (checkIfCorrectECL(elem1[1])):
					list[5] = True
			elif (elem1[0] == "pid"):
				if (checkIfCorrectPID(elem1[1])):
					list[6] = True
			elif (elem1[0] == "cid"):
				list[7] = True

if ( (list == [True, True, True, True, True, True, True, False]) or ((list == [True, True, True, True, True, True, True, True])) ):
	counter += 1

print(counter)