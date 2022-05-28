with open("input.txt") as f:
    lines = f.readlines()

syntax_error_score = 0

for line in lines:
    history = []
    for char in line:
        if (char == "("):
            history.append("(")
        elif (char == "["):
            history.append("[")
        elif (char == "{"):
            history.append("{")
        elif (char == "<"):
            history.append("<")

        elif (char == ")"):
            if history[-1] == "(":
                history.pop()
            else:
                syntax_error_score += 3
                break
        elif (char == "]"):
            if history[-1] == "[":
                history.pop()
            else:
                syntax_error_score += 57
                break
        elif (char == "}"):
            if history[-1] == "{":
                history.pop()
            else:
                syntax_error_score += 1197
                break
        elif (char == ">"):
            if history[-1] == "<":
                history.pop()
            else:
                syntax_error_score += 25137
                break

print(syntax_error_score)