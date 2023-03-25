# Zadanie 4.2
import time
st = time.time()


def find_dev_number(n):
    dev_numbers_array = []
    k = 2
    while n != 1:
        while n % k == 0:
            n //= k
            dev_numbers_array.append(k)
        k += 1
    return dev_numbers_array


helper_array = []
file_numbers = []
helper_array_2 = []

with open("liczby.txt") as file:
    prime_count = 0
    for line in file:
        base = line.strip().split()
        for num in base:
            file_numbers.append(num)
            helper_array.append(len(find_dev_number(int(num))))
            helper_array_2.append(find_dev_number(int(num)))

print(file_numbers[max(helper_array)])
print(max(helper_array))

count_dif_array = []

for number in helper_array_2:
    only_dif = list(set(number))
    count_dif_array.append(len(only_dif))

print(file_numbers[count_dif_array.index(max(count_dif_array))])
print(max(count_dif_array))

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
file.close()
