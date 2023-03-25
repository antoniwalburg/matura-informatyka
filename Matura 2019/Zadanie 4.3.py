temp = []
with open('przyklad.txt') as file:
    for line in file:
        base = line.strip().split()
        for number in base:
            temp.append(int(number))

ex = []
for i in temp:
    for j in temp:
        if i % j == 0:
            ex.append([i,j])
nex = []
for x in ex:
    for y in x:
        nex.append(y)
k = []
for i in nex:
    x = nex.count(i)
    k.append(x)
max_index = max(k)
nex_nex = sorted(nex)
print(nex_nex[max_index-1])