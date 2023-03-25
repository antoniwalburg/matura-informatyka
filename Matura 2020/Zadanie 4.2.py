strings = []

with open('pary.txt') as file:
    for line in file:
        base = line.rstrip().split()
        strings.append(base[1])
print(strings)

arr = []


def longest_repeating_letters(s):
    max_substring = ""
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            substring = s[i:j]
            if substring.count(substring[0]) == len(substring):
                if len(substring) > len(max_substring):
                    max_substring = substring
    return max_substring


for x in strings:
    print(longest_repeating_letters(x), len(longest_repeating_letters(x)))
