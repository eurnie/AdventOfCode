def calculateResult(input):
	with open(input) as f:
		lines = f.readlines()
	counter = 0
	for line in lines:
		result = simplifyExpression(line)
		counter += int(result)
	return counter

def simplifyExpression(line):
	if (not ('(' in line)):
		return str(evaluateExpression(line.split(" ")))
	else:
		bracketCounter = 0
		start = False
		startPos = 'null'
		endPos = 'null'
		iterator = 0
		while (bracketCounter != 0) or (not start):
			if (line[iterator] == '(') and (not start):
				start = True
				bracketCounter += 1
				startPos = iterator
			elif (line[iterator] == '(') and (start):
				bracketCounter += 1
			elif (line[iterator] == ')'):
				bracketCounter -= 1
				endPos = iterator
			iterator += 1
		newExpr = line[:startPos] + simplifyExpression(line[startPos+1:endPos]) + line[endPos+1:]
		return simplifyExpression(newExpr)

def evaluateExpression(expression):
	counter = int(expression[0])
	for i in range(1, len(expression)-1):
		if (expression[i] == '+'):
			counter += int(expression[i+1])
		elif (expression[i] == '*'):
			counter *= int(expression[i+1])
	return counter

print(calculateResult('input.txt'))