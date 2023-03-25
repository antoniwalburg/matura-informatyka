def Mirror(n):
    str_n = str(n)
    new_n = str_n[::-1]
    return int(new_n)


mirror_array = []
array = []

with open("liczby.txt") as file:
    for line in file:
        base = line.strip().split()
        for number in base:
            mirror_array.append(abs(Mirror(int(number)) - int(number)))
            array.append(int(number))

print(array[mirror_array.index(max(mirror_array))])
print(max(mirror_array))