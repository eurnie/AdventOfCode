def doAction(state, action):
	if (state == "1"):
		if (action == "R"): return "1"
		elif (action == "D"): return "3"
		elif (action == "L"): return "1"
		elif (action == "U"): return "1"
	elif (state == "2"):
		if (action == "R"): return "3"
		elif (action == "D"): return "6"
		elif (action == "L"): return "2"
		elif (action == "U"): return "2"
	elif (state == "3"):
		if (action == "R"): return "4"
		elif (action == "D"): return "7"
		elif (action == "L"): return "2"
		elif (action == "U"): return "1"
	elif (state == "4"):
		if (action == "R"): return "4"
		elif (action == "D"): return "8"
		elif (action == "L"): return "3"
		elif (action == "U"): return "4"
	elif (state == "5"):
		if (action == "R"): return "6"
		elif (action == "D"): return "5"
		elif (action == "L"): return "5"
		elif (action == "U"): return "5"
	elif (state == "6"):
		if (action == "R"): return "7"
		elif (action == "D"): return "A"
		elif (action == "L"): return "5"
		elif (action == "U"): return "2"
	elif (state == "7"):
		if (action == "R"): return "8"
		elif (action == "D"): return "B"
		elif (action == "L"): return "6"
		elif (action == "U"): return "3"
	elif (state == "8"):
		if (action == "R"): return "9"
		elif (action == "D"): return "C"
		elif (action == "L"): return "7"
		elif (action == "U"): return "4"
	elif (state == "9"):
		if (action == "R"): return "9"
		elif (action == "D"): return "9"
		elif (action == "L"): return "8"
		elif (action == "U"): return "9"
	elif (state == "A"):
		if (action == "R"): return "B"
		elif (action == "D"): return "A"
		elif (action == "L"): return "A"
		elif (action == "U"): return "6"
	elif (state == "B"):
		if (action == "R"): return "C"
		elif (action == "D"): return "D"
		elif (action == "L"): return "A"
		elif (action == "U"): return "7"
	elif (state == "C"):
		if (action == "R"): return "C"
		elif (action == "D"): return "C"
		elif (action == "L"): return "B"
		elif (action == "U"): return "8"
	elif (state == "D"):
		if (action == "R"): return "D"
		elif (action == "D"): return "D"
		elif (action == "L"): return "D"
		elif (action == "U"): return "B"

with open('input.txt') as f:
    lines = f.readlines()

result = ""
state = "5"

for line in lines:
	line = line.rstrip("\n")
	for elem in line:
		state = doAction(state, elem)
	result += state

print(result)