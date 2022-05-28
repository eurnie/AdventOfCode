with open("input.txt") as f:
    lines = f.readlines()

autocompletion_scores = []

for line in lines:
    history = []
    autocompletion_needed = True
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
                autocompletion_needed = False
                break
        elif (char == "]"):
            if history[-1] == "[":
                history.pop()
            else:
                autocompletion_needed = False
                break
        elif (char == "}"):
            if history[-1] == "{":
                history.pop()
            else:
                autocompletion_needed = False
                break
        elif (char == ">"):
            if history[-1] == "<":
                history.pop()
            else:
                autocompletion_needed = False
                break

    if autocompletion_needed:
        score = 0
        while len(history) != 0:
            if history[-1] == "(":
                score = (score * 5) + 1
            elif history[-1] == "[":
                score = (score * 5) + 2
            elif history[-1] == "{":
                score = (score * 5) + 3
            elif history[-1] == "<":
                score = (score * 5) + 4
            history.pop()
        autocompletion_scores.append(score)

autocompletion_scores.sort()
print(autocompletion_scores[round(len(autocompletion_scores) / 2) - 1])