def executeProgram(program):
	myprogram = [int(number) for number in program]
	for i in range(0, len(myprogram) - 1, 4):
		if (myprogram[i] == 1):
			myprogram[myprogram[i+3]] = myprogram[myprogram[i+1]] + myprogram[myprogram[i+2]]
		elif (myprogram[i] == 2):
			myprogram[myprogram[i+3]] = myprogram[myprogram[i+1]] * myprogram[myprogram[i+2]]
		elif (myprogram[i] == 99):
			break;
		else:
			print("command not known")
			break;
	return myprogram

with open('input.txt') as f:
	firstLine = f.readline()

print(executeProgram(firstLine[:-1].split(","))[0])