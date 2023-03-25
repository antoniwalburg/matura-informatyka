# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Zadanie 4.1
with open('liczby.txt') as file:
    main_counter = 0
    for line in file:
        base = line.strip().split()
        for bin_num in base:
            count_zero = bin_num.count("0")
            count_one = bin_num.count("1")
        if count_zero > count_one:
            main_counter += 1
    print(main_counter)
file.close()