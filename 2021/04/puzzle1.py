def createBingoCards(input):
    bingo_cards = []
    new_card = []
    
    for i in range(2,len(lines)):
        if (lines[i] == "\n"):
            bingo_cards.append(new_card)
            new_card = []
        else:
            line_splitted = lines[i][0:len(lines[i])-1].split(" ")
            line_splitted = [x for x in line_splitted if x]
            new_row = []
            for element in line_splitted:
                new_row.append([element, False])
            new_card.append(new_row)

    bingo_cards.append(new_card)
    return bingo_cards

def createListOfNumbers(input):
    return lines[0][0:len(lines[0])-1].split(",")

def checkIfRowCompleted(card):
    for row in card:
        allTrue = True
        for element in row:
            if (element[1] == False):
                allTrue = False
        if allTrue:
            break
    return allTrue

def checkIfColumnCompleted(card):
    for i in range(0, len(card[0])):
        allTrue = True
        for j in range(0, len(card)):
            if (card[j][i][1] == False):
                allTrue = False
        if (allTrue):
            break
    return allTrue

def checkIfSomeoneHasBingo(bingo_cards):
    listOfBingoCarsIndexes = []
    for i in range(0, len(bingo_cards)):
        if (checkIfRowCompleted(bingo_cards[i]) or checkIfColumnCompleted(bingo_cards[i])):
            listOfBingoCarsIndexes.append(i)
    if (not len(listOfBingoCarsIndexes) == 0):
        return [True, listOfBingoCarsIndexes[0]]
    else:
        return [False, 0]

def sumOfAllUnmarkedNumbers(card):
    count = 0
    for row in card:
        for element in row:
            if (element[1] == False):
                count += int(element[0])
    return count

with open('input.txt') as f:
    lines = f.readlines()

numbers = createListOfNumbers(lines)
bingo_cards = createBingoCards(lines)
someoneHasBingo = False
personWhoHasBingo = 0
numberIndex = 0

while (not someoneHasBingo):
    number = numbers[numberIndex]
    for card in bingo_cards:
        for row in card:
            for element in row:
                if (int(element[0]) == int(number)):
                    element[1] = True
   
    checkResult = checkIfSomeoneHasBingo(bingo_cards)
    someoneHasBingo = checkResult[0]
    if (not someoneHasBingo):
        numberIndex += 1
    else:
        personWhoHasBingo = checkResult[1]

print(sumOfAllUnmarkedNumbers(bingo_cards[personWhoHasBingo]) * int(numbers[numberIndex]))