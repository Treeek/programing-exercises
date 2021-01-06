# source: https://cses.fi/problemset/result/775261/

n = int(input())
lines = input().split()
total = 0
for number in lines:
    total += int(number)
 
def sum(n):
    return n * (n + 1) // 2
print(sum(n) - total)