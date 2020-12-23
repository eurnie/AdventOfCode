import copy 

def createListPlayer(input, playerName):
	with open(input) as f:
		lines = f.readlines()
	returnList = []
	active = False
	for line in lines:
		if (line == '\n'):
			active = False
		if (active):
			returnList.append(int(line[:-1]))
		if (playerName in line):
			active = True
	return returnList

def playRound(player1, player2):
	listPlayer1 = copy.deepcopy(player1)
	listPlayer2 = copy.deepcopy(player2)
	cartPlayer1 = listPlayer1.pop(0)
	cartPlayer2 = listPlayer2.pop(0)
	if (cartPlayer1 > cartPlayer2):
		listPlayer1.append(cartPlayer1)
		listPlayer1.append(cartPlayer2)
	elif (cartPlayer2 > cartPlayer1):
		listPlayer2.append(cartPlayer2)
		listPlayer2.append(cartPlayer1)
	if (len(listPlayer1) == 0):
		return listPlayer2
	elif (len(listPlayer2) == 0):
		return listPlayer1
	else:
		return playRound(listPlayer1, listPlayer2)

def calculateResult(givenList):
	counter = 0
	for i in range(len(givenList), 0, -1):
		counter += i * givenList[len(givenList) - i]
	return counter

print(calculateResult(playRound(createListPlayer('input.txt', 'Player 1:'), createListPlayer('input.txt', 'Player 2:'))))