def isPrime(num):
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if (num % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False


def Mirror(n):
    str_n = str(n)
    new_n = str_n[::-1]
    return int(new_n)


with open("liczby.txt") as file:
    for line in file:
        base = line.strip().split()
        for number in base:
            if isPrime(int(number)) and isPrime(Mirror(int(number))):
                print(number)
