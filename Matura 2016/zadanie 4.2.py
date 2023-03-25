# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Zadanie 4.2
with open('liczby.txt') as file:
    by_two_counter = 0
    by_eight_counter = 0
    for line in file:
        base = line.strip().split()
        for bin_num in base:
            if bin_num[-1] == "0" and len(bin_num) > 1:
                by_two_counter += 1
                if bin_num[-2] == "0" and bin_num[-3] == "0":
                    by_eight_counter += 1
    print("Ilość liczb podzielnych przez dwa(2):", by_two_counter)
    print("Ilość liczb podzielnych przez osiem(8):", by_eight_counter)

file.close()