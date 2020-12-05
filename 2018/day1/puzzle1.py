lines = []

with open('input.txt') as f:
    lines = f.readlines()

count = 0

for line in lines:
    count += int(line)

print(count)
