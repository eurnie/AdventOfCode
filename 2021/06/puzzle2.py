def cleanFishList(fishList):
    fish0 = 0
    fish1 = 0
    fish2 = 0
    fish3 = 0
    fish4 = 0
    fish5 = 0
    fish6 = 0
    fish7 = 0
    fish8 = 0

    for x in range(0, len(fishList)):
        if (fishList[x][0] == 0):
            fish0 += fishList[x][1]
        elif (fishList[x][0] == 1):
            fish1 += fishList[x][1]
        elif (fishList[x][0] == 2):
            fish2 += fishList[x][1]
        elif (fishList[x][0] == 3):
            fish3 += fishList[x][1]
        elif (fishList[x][0] == 4):
            fish4 += fishList[x][1]
        elif (fishList[x][0] == 5):
            fish5 += fishList[x][1]
        elif (fishList[x][0] == 6):
            fish6 += fishList[x][1]
        elif (fishList[x][0] == 7):
            fish7 += fishList[x][1]
        elif (fishList[x][0] == 8):
            fish8 += fishList[x][1]

    return [[0, fish0], [1, fish1], [2, fish2], [3, fish3], [4, fish4], [5, fish5], [6, fish6], [7, fish7], [8, fish8]]

with open("input.txt") as f:
    lines = f.readlines()

fishList = lines[0][0:len(lines[0])-1].split(",")

for i in range(0, len(fishList)):
    fishList[i] = [int(fishList[i]), 1]

for i in range(0, 256):
    addList = []
    for x in range(0, len(fishList)):
        if (fishList[x][0] == 0):
            addList.append([8, fishList[x][1]])
            fishList[x][0] = 6
        else:
            fishList[x][0] -= 1

    fishList += addList
    fishList = cleanFishList(fishList)

count = 0
for elem in fishList:
    count += elem[1]

print(count)