# source: https://cses.fi/problemset/task/1755/

string = input()
occurrences = {}
left = ""
middle = ""
for c in string:
    occurrences[c] = occurrences.get(c, 0) + 1
for c in occurrences.keys():
    occurrence = occurrences[c]
    if occurrence % 2 == 0:
        left += (occurrence // 2) * c
    else:
        if middle:
            print("NO SOLUTION")
            exit()
        middle = occurrence * c
print(left + middle + left[::-1])