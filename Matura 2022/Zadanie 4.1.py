# Zadanie 4.1
with open("liczby.txt") as file:
    count_numbers = 0
    helper_array = []
    for line in file:
        base = line.strip().split()
        for num in base:
            if num[0] == num[-1]:
                count_numbers += 1
                helper_array.append(num)
    first_good_number = helper_array[0]

    print(count_numbers)
    print(first_good_number)

