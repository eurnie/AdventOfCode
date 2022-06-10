def print_dict(dictionary):
    print("----------")
    for key in dictionary:
        print(key, dictionary[key])
    print("----------")

def is_coverged(dictionary):
    for key in dictionary:
        if len(dictionary[key]) != 1:
            return False
    return True

def convert_to_number(number_string, dictionary):
    original_string = ""
    number = 10
    
    for char in number_string:
        original_string += dictionary[char][0]
    
    original_string = ''.join(sorted(original_string))

    if (original_string == "abcefg"):
        number = "0"
    elif (original_string == "cf"):
        number = "1"
    elif (original_string == "acdeg"):
        number = "2"
    elif (original_string == "acdfg"):
        number = "3"
    elif (original_string == "bcdf"):
        number = "4"
    elif (original_string == "abdfg"):
        number = "5"
    elif (original_string == "abdefg"):
        number = "6"
    elif (original_string == "acf"):
        number = "7"
    elif (original_string == "abcdefg"):
        number = "8"
    elif (original_string == "abcdfg"):
        number = "9"

    return str(number)

with open("input.txt") as f:
    lines = f.readlines()

total_sum = 0

for line in lines:

    wire_to_segment_dictionary = {
        "a": ["a", "b", "c", "d", "e", "f", "g"],
        "b": ["a", "b", "c", "d", "e", "f", "g"],
        "c": ["a", "b", "c", "d", "e", "f", "g"],
        "d": ["a", "b", "c", "d", "e", "f", "g"],
        "e": ["a", "b", "c", "d", "e", "f", "g"],
        "f": ["a", "b", "c", "d", "e", "f", "g"],
        "g": ["a", "b", "c", "d", "e", "f", "g"],
    }

    splitted = line.split("|")
    first_part = splitted[0].split(" ")[:-1]
    second_part = splitted[1].split(" ")[1:]

    for i in range(len(second_part)):
        second_part[i] = second_part[i].replace("\n","")

    while (not is_coverged(wire_to_segment_dictionary)):
        remember_5 = []
        remember_6 = []
        remember_all = [] 

        for code in first_part:
            to_remove = []
            to_remove_from_all = []

            if len(code) == 2:
                to_remove.append("a")
                to_remove.append("b")
                to_remove.append("d")
                to_remove.append("e")
                to_remove.append("g")
            elif len(code) == 3:
                to_remove.append("b")
                to_remove.append("d")
                to_remove.append("e")
                to_remove.append("g")
            elif len(code) == 4:
                to_remove.append("a")
                to_remove.append("e")
                to_remove.append("g")
            elif len(code) == 5:
                remember_5.append(code[0])
                remember_5.append(code[1])
                remember_5.append(code[2])
                remember_5.append(code[3])
                remember_5.append(code[4])
            elif len(code) == 5:
                remember_6.append(code[0])
                remember_6.append(code[1])
                remember_6.append(code[2])
                remember_6.append(code[3])
                remember_6.append(code[4])
                remember_6.append(code[5])

            for i in range(len(code)):
                remember_all.append(code[i])

            for key in wire_to_segment_dictionary:
                if len(wire_to_segment_dictionary[key]) == 1:
                    to_remove_from_all.append([[key], wire_to_segment_dictionary[key][0]])

            for key1 in wire_to_segment_dictionary:
                for key2 in wire_to_segment_dictionary:
                    if (key1 != key2):
                        if (wire_to_segment_dictionary[key1] == wire_to_segment_dictionary[key2]) and (len(wire_to_segment_dictionary[key1]) == 2):
                            to_remove_from_all.append([[key1, key2], wire_to_segment_dictionary[key1][0]])
                            to_remove_from_all.append([[key1, key2], wire_to_segment_dictionary[key1][1]])

            for char in code:
                for element in to_remove:
                    if element in wire_to_segment_dictionary[char]:
                        wire_to_segment_dictionary[char].remove(element)

            for char in wire_to_segment_dictionary:
                for element in to_remove_from_all:
                    if not char in element[0]:
                        if element[1] in wire_to_segment_dictionary[char]:
                            wire_to_segment_dictionary[char].remove(element[1])

        counts_5 = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
        }

        counts_6 = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
        }

        counts_all = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
        }

        for element in remember_5:
            counts_5[element] += 1

        for element in remember_6:
            counts_6[element] += 1

        for element in remember_all:
            counts_all[element] += 1

        for key in counts_5:
            remove_list = []
            if counts_5[key] == 3:
                remove_list.append("b")
                remove_list.append("c")
                remove_list.append("e")
                remove_list.append("f")
            elif counts_5[key] == 2:
                remove_list.append("a")
                remove_list.append("d")
                remove_list.append("g")
                
            for elem in remove_list:
                if elem in wire_to_segment_dictionary[key]:
                    wire_to_segment_dictionary[key].remove(elem)

        for key in counts_6:
            remove_list = []
            if counts_6[key] == 3:
                remove_list.append("c")
                remove_list.append("d")
                remove_list.append("e")
            elif counts_6[key] == 2:
                remove_list.append("a")
                remove_list.append("b")
                remove_list.append("f")
                remove_list.append("g")

            for elem in remove_list:
                if elem in wire_to_segment_dictionary[key]:
                    wire_to_segment_dictionary[key].remove(elem)

        for key in counts_all:
            remove_list = []

            if counts_all[key] == 4:
                remove_list.append("a")
                remove_list.append("b")
                remove_list.append("c")
                remove_list.append("d")
                remove_list.append("f")
                remove_list.append("g")
            elif counts_all[key] == 6:
                remove_list.append("a")
                remove_list.append("c")
                remove_list.append("d")
                remove_list.append("e")
                remove_list.append("f")
                remove_list.append("g")
            elif counts_all[key] == 7:
                remove_list.append("a")
                remove_list.append("b")
                remove_list.append("c")
                remove_list.append("e")
                remove_list.append("f")
            elif counts_all[key] == 8:
                remove_list.append("b")
                remove_list.append("d")
                remove_list.append("e")
                remove_list.append("f")
                remove_list.append("g")
            elif counts_all[key] == 9:
                remove_list.append("a")
                remove_list.append("b")
                remove_list.append("c")
                remove_list.append("d")
                remove_list.append("e")
                remove_list.append("g")

            for elem in remove_list:
                if elem in wire_to_segment_dictionary[key]:
                    wire_to_segment_dictionary[key].remove(elem)

    string = ""
    for element in second_part:
        string += convert_to_number(element, wire_to_segment_dictionary)

    total_sum += int(string)

print(total_sum)