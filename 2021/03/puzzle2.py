import copy

def mostCommonBit(list_of_binary_numbers, position, preference): 
    result = ""
    nb_of_zeros = 0
    nb_of_ones = 0

    for element in list_of_binary_numbers:
        if element[position] == "0":
            nb_of_zeros += 1
        if element[position] == "1":
            nb_of_ones += 1

    if (nb_of_zeros > nb_of_ones):
        if (preference == "1"):
            result += "0"
        else:
            result += "1"
    elif (nb_of_ones > nb_of_zeros):
        if (preference == "1"):
            result += "1"
        else:
            result += "0"
    elif (nb_of_ones == nb_of_zeros):
        result += preference

    return result

def calculateRating(list_of_binary_numbers, preference):
    resulting_list = copy.deepcopy(list_of_binary_numbers)
    delete_list = []
    i = 0

    while len(resulting_list) > 1:
        most_common_bit = mostCommonBit(resulting_list, i, preference)
        for element in resulting_list:
            if (element[i] != most_common_bit):
                delete_list.append(element)
        for x in delete_list:
            if (x in resulting_list):
                resulting_list.remove(x)
        i += 1

    return int(resulting_list[0], 2)

with open('input.txt') as f:
    lines = f.readlines()

print(calculateRating(lines, "0") * calculateRating(lines, "1"))