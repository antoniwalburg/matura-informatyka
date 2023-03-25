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


even_array = []

with open('pary.txt') as file:
    for line in file:
        base = line.strip().split()
        if int(base[0]) % 2 == 0:
            even_array.append(int(base[0]))

for i in even_array:
    flag = False
    for j in range(1, i):
        if flag:
            break
        else:
            for k in range(1, i):
                if isPrime(j) and isPrime(k):
                    if j + k == i:
                        print(i,j,k)
                        flag = True

