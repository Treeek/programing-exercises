# source: https://cses.fi/problemset/task/1071

def find(y, x):
    hightest = max(x, y)
    lowest = min(x, y)
    if ((y == hightest and y % 2 == 0) or (x == hightest and x % 2 != 0)):
        return hightest ** 2 - lowest + 1
    return hightest ** 2 - 2 * hightest + lowest + 1
 
n = int(input())
inputs = []
for i in range(0, n):
    line = input().split()
    inputs.append(
        [
            int(line[0]),
            int(line[1])
        ]
    )
 
for i in inputs:
    y = i[0]
    x = i[1]
    print(find(y, x))