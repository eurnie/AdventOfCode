with open("input.txt") as f:
    lines = f.readlines()

fishList = lines[0][0:len(lines[0])-1].split(",")

for i in range(0, len(fishList)):
    fishList[i] = int(fishList[i])

for i in range(0, 80):
    addList = []
    for x in range(0, len(fishList)):
        if (fishList[x] == 0):
            addList.append(8)
            fishList[x] = 6
        else:
            fishList[x] -= 1

    fishList += addList

print(len(fishList))