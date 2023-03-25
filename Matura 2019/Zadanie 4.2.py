import math


def factor(n):
    list_of_digits = []
    for x in str(n):
        list_of_digits.append(int(x))
    for i in range(len(list_of_digits)):
        list_of_digits[i] = math.factorial(list_of_digits[i])
    if sum(list_of_digits) == int(n):
        return True
    else:
        return False


with open('liczby.txt') as file:
    for line in file:
        base = line.strip().split()
        for number in base:
            if factor(number):
                print(number)
