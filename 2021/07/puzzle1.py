def highestValue(givenList):
    highest = 0

    for i in range(0, len(givenList)):
        if (givenList[i] > highest):
            highest = givenList[i]

    return highest

with open("input.txt") as f:
    lines = f.readlines()

positionsList = lines[0][0:len(lines[0])-1].split(",")

for i in range(0, len(positionsList)):
    positionsList[i] = int(positionsList[i])

bestDifference = 0
for i in range(0, len(positionsList)):
    bestDifference += positionsList[i]

for x in range(0, highestValue(positionsList)):
    difference = 0
    for y in range(0, len(positionsList)):
        difference += abs(x - positionsList[y])
    if (difference < bestDifference):
        bestDifference = difference

print(bestDifference)