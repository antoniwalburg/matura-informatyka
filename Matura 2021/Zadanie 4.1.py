# Zadanie 1,2,3,4

with open('instrukcje.txt') as file:
    output_string = []
    ans = ""
    for line in file:
        base = line.strip().split()
        count = 0
        if base[0] == "DOPISZ":
            output_string.append(base[1])
        elif base[0] == "ZMIEN":
            output_string.pop()
            output_string.append(base[1])
        elif base[0] == "USUN":
            output_string.pop()
        elif base[0] == "PRZESUN" and base[1] != "Z" and base[1] in output_string:
            get_number = ord(base[1]) + 1
            output_string[output_string.index(base[1])] = chr(get_number)
        elif base[0] == "PRZESUN" and base[1] == "Z" and base[1] in output_string:
            output_string[output_string.index(base[1])] = "A"
    for letter in output_string:
        ans += letter

    print(ans)



