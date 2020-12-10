import copy

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
	if (position == len(program)):
		return (True, accumulator)
	line = program[position]
	if(line[2] == True):
		return (False, accumulator)
	else:
		if (line[0] == 'nop'):
			line[2] = True
			return executeLine(position + 1, program, accumulator)
		elif (line[0] == 'acc'):
			line[2] = True
			return executeLine(position + 1, program, accumulator + int(line[1]))
		elif (line[0] == 'jmp'):
			line[2] = True
			return executeLine(position + int(line[1]), program, accumulator)

def checkAllChanges(program):
	for position in range(0, len(program) - 1):
		if (program[position][0] == 'nop'):
			newProgram = copy.deepcopy(program)
			newProgram[position][0] = 'jmp'
			result = executeLine(0, newProgram, 0)
			if (result[0]):
				print(result[1])
				break
		if (program[position][0] == 'jmp'):
			newProgram = copy.deepcopy(program)
			newProgram[position][0] = 'nop'
			result = executeLine(0, newProgram, 0)
			if (result[0]):
				print(result[1])
				break

checkAllChanges(createProgram('input.txt'))