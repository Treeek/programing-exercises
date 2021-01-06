# source: https://cses.fi/problemset/task/1069

DNA = input()
total = 1
highest = 1
current = DNA[0]
 
for char in DNA[1:]:
    if char == current:
        total += 1
        if total > highest:
            highest = total
    else:
        if total > highest:
            highest = total
        current = char
        total = 1
 
print(highest)