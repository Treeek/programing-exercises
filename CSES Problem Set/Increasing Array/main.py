# source: https://cses.fi/problemset/task/1094/

n = int(input())
inputs = [int(x) for x in input().split()]
 
output = 0
hightest = 0
 
for i in inputs:
    hightest = max(i, hightest)
    output += hightest - i
 
print(output)