# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Zadanie 4.3
import time

with open('liczby.txt') as file:
    st = time.time()
    real_numbers = []
    for line in file:
        base = line.strip().split()
        for bin_num in base:
            real_numbers.append(int(bin_num,2))
    # Min
    print("Najmniejsza liczba to:", real_numbers.index(min(real_numbers)) + 1)
    # Max
    print("Największa liczba to:",real_numbers.index(max(real_numbers)) + 1)
    et = time.time()
    elapsed_time = et - st
    print('Execution time:', elapsed_time, 'seconds')
file.close()