with open("input.txt") as f:
    lines = f.readlines()

total_count = 0

for line in lines:
    splitted = line.split("|")[1].split(" ")
    for element in splitted:
        clean_element = element.replace("\n","")
        if (len(clean_element) == 7) or (len(clean_element) == 4) or (len(clean_element) == 3) or (len(clean_element) == 2):
            total_count += 1

print(total_count)