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
				list[0] = True
			elif (elem1[0] == "iyr"):
				list[1] = True
			elif (elem1[0] == "eyr"):
				list[2] = True
			elif (elem1[0] == "hgt"):
				list[3] = True
			elif (elem1[0] == "hcl"):
				list[4] = True
			elif (elem1[0] == "ecl"):			
				list[5] = True
			elif (elem1[0] == "pid"):
				list[6] = True
			elif (elem1[0] == "cid"):
				list[7] = True

if ( (list == [True, True, True, True, True, True, True, False]) or ((list == [True, True, True, True, True, True, True, True])) ):
	counter += 1

print(counter)