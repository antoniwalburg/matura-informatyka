# Zadanie 4.1

def Mirror(n):
    str_n = str(n)
    new_n = str_n[::-1]
    return int(new_n)


numbers_array = []
mirror_numbers = []

with open("liczby.txt") as file:
    for line in file:
        base = line.strip().split()
        for number in base:
            numbers_array.append(int(number))

for i in numbers_array:
    mirror_numbers.append(Mirror(i))

for j in mirror_numbers:
    if j % 17 == 0:
        print(j)
    else:
        continue

file.close()