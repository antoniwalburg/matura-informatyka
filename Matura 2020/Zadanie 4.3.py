temp = []

with open('pary.txt') as file:
    for line in file:
        base = line.strip().split()
        if int(base[0]) == len(base[1]):
            temp.append([int(base[0]),base[1]])
sorted_temp = sorted(temp)
print(sorted_temp[0])