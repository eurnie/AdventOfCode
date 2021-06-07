def doAction(state, action):
	if (state == 1):
		if (action == "R"): return 2
		elif (action == "D"): return 4
		elif (action == "L"): return 1
		elif (action == "U"): return 1
	elif (state == 2):
		if (action == "R"): return 3
		elif (action == "D"): return 5
		elif (action == "L"): return 1
		elif (action == "U"): return 2
	elif (state == 3):
		if (action == "R"): return 3
		elif (action == "D"): return 6
		elif (action == "L"): return 2
		elif (action == "U"): return 3
	elif (state == 4):
		if (action == "R"): return 5
		elif (action == "D"): return 7
		elif (action == "L"): return 4
		elif (action == "U"): return 1
	elif (state == 5):
		if (action == "R"): return 6
		elif (action == "D"): return 8
		elif (action == "L"): return 4
		elif (action == "U"): return 2
	elif (state == 6):
		if (action == "R"): return 6
		elif (action == "D"): return 9
		elif (action == "L"): return 5
		elif (action == "U"): return 3
	elif (state == 7):
		if (action == "R"): return 8
		elif (action == "D"): return 7
		elif (action == "L"): return 7
		elif (action == "U"): return 4
	elif (state == 8):
		if (action == "R"): return 9
		elif (action == "D"): return 8
		elif (action == "L"): return 7
		elif (action == "U"): return 5
	elif (state == 9):
		if (action == "R"): return 9
		elif (action == "D"): return 9
		elif (action == "L"): return 8
		elif (action == "U"): return 6

with open('input.txt') as f:
    lines = f.readlines()

result = ""
state = 5

for line in lines:
	line = line.rstrip("\n")
	for elem in line:
		state = doAction(state, elem)
	result += str(state)

print(result)