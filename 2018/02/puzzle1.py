with open('input.txt') as f:
    lines = f.readlines()

number_times_2 = 0
number_times_3 = 0
character_times = []

for line in lines:
    for character in line:
    	if (character, 1) in character_times:
    		character_times.append((character, 2))
    		character_times.remove((character, 1))
    	elif (character, 2) in character_times:
    		character_times.append((character, 3))
    		character_times.remove((character, 2))
    	else:
    		character_times.append((character, 1))

    added_2 = False
    added_3 = False

    for elem in character_times:
    	if ( (elem[1] == 2) and (not added_2) ):
    		number_times_2 += 1
    		added_2 = True
    	elif ( (elem[1] == 3) and (not added_3) ):
    		number_times_3 += 1
    		added_3 = True

    character_times = []

result = number_times_2 * number_times_3
print(result)
