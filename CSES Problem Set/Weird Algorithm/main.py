n = int(input())
output = [str(n)]
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1
    output.append(str(n))
    pass
output = " ".join(output)
print(output)