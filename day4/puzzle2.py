def removeNewLineCharacter(input):
	output = input
	lastCharacter = output[-1]
	if (lastCharacter == "\n"):
		output = output[:-1]
	return output

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
	input = removeNewLineCharacter(input)
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
	input = removeNewLineCharacter(input)
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
	if ((input == "a") or (input == "b") or (input == "b") or 
		(input == "c") or (input == "d") or (input == "e") or 
		(input == "f")):
		return True
	return False

def checkIfCorrectECL(input):
	input = removeNewLineCharacter(input)
	if ((input == "amb") or (input == "blu") or (input == "brn") or 
		(input == "gry") or (input == "grn") or (input == "hzl") or 
		(input == "oth")):
		return True
	return False

def checkIfCorrectPID(input):
	input = removeNewLineCharacter(input)
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
			if ((elem1[0] == "byr") and (checkIfCorrectBYR(elem1[1]))):
					list[0] = True
			elif ((elem1[0] == "iyr") and (checkIfCorrectIYR(elem1[1]))):
					list[1] = True
			elif ((elem1[0] == "eyr") and (checkIfCorrectEYR(elem1[1]))):
					list[2] = True
			elif ((elem1[0] == "hgt") and (checkIfCorrectHGT(elem1[1]))):
					list[3] = True
			elif ((elem1[0] == "hcl") and (checkIfCorrectHCL(elem1[1]))):
					list[4] = True
			elif ((elem1[0] == "ecl") and (checkIfCorrectECL(elem1[1]))):
					list[5] = True
			elif ((elem1[0] == "pid") and (checkIfCorrectPID(elem1[1]))):
					list[6] = True
			elif (elem1[0] == "cid"):
				list[7] = True

if ( (list == [True, True, True, True, True, True, True, False]) or ((list == [True, True, True, True, True, True, True, True])) ):
	counter += 1

print(counter)