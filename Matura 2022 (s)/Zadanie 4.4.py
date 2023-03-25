numbers_array = []
sample = []

with open("liczby.txt") as file:
    for line in file:
        base = line.strip().split()
        for number in base:
            numbers_array.append(int(number))

non_duplicates_numbers_array = list(set(numbers_array))
# p1
print(len(non_duplicates_numbers_array))
# p2
for i in numbers_array:
    sample.append(numbers_array.count(i))
print(round(sample.count(2)/2))
# p3
print(round(sample.count(3)/3))