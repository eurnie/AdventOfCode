def createProgram(input):
	with open(input) as f:
		lines = f.readlines()
	program = []
	for line in lines:
		splitted = line[:-1].split(" ")
		splitted.append(False)
		program.append(splitted)
	return program

def executeLine(position, program, accumulator):
	line = program[position]
	if(line[2] == True):
		print(accumulator)
	else:
		if (line[0] == 'nop'):
			line[2] = True
			executeLine(position + 1, program, accumulator)
		elif (line[0] == 'acc'):
			line[2] = True
			executeLine(position + 1, program, accumulator + int(line[1]))
		elif (line[0] == 'jmp'):
			line[2] = True
			executeLine(position + int(line[1]), program, accumulator)

executeLine(0, createProgram('input.txt'), 0)