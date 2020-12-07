def executeProgram(program):
	prgrm = program
	for i in range(0, len(prgrm) - 1, 4):
		if (prgrm[i] == 1):
			prgrm[prgrm[i+3]] = prgrm[prgrm[i+1]] + prgrm[prgrm[i+2]]
		elif (prgrm[i] == 2):
			prgrm[prgrm[i+3]] = prgrm[prgrm[i+1]] * prgrm[prgrm[i+2]]
		elif (prgrm[i] == 99):
			break;
	return prgrm

with open('input.txt') as f:
	firstLine = f.readline()

for noun in range(0, 99):
	for verb in range(0, 99):
		program = firstLine[:-1].split(",")
		myprogram = [int(number) for number in program]
		myprogram[1] = noun
		myprogram[2] = verb
		if (executeProgram(myprogram)[0] == 19690720):
			print((100 * noun) + verb)