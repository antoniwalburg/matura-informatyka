# Zadanie 4.3

count_good_numbers = 0
with open("przyklad.txt") as file:
    file_nums = []
    prime_count = 0
    for line in file:
        base = line.strip().split()
        for num in base:
            file_nums.append(int(num))

    print(file_nums)
    print(file_nums)
    print(file_nums)
file.close()