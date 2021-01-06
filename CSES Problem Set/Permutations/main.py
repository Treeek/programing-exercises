# source: https://cses.fi/problemset/task/1070

n = int(input())
output = list()
 
if n == 4:
    print('2 4 1 3')
elif n == 1:
    print('1')
elif n < 5:
    print("NO SOLUTION")
else:
    for i in range(1, n + 1, 2):
        output.append(str(i))
    for i in range(2, n + 1, 2):
        output.append(str(i))
    print(' '.join(output))