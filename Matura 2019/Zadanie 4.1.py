table = []
for x in range(0,11):
    table.append(3 ** x)

with open('liczby.txt') as file:
    count_pow = 0
    for line in file:
        base = line.strip().split()
        for number in base:
            if int(number) in table:
                count_pow += 1
print(count_pow)
