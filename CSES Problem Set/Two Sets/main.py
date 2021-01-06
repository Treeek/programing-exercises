# source: https://cses.fi/problemset/task/1092

n = int(input())
# inputs = [int(x) for x in input().split()]
 
def sum(n):
    return n * (n + 1) // 2
 
if (sum(n) % 2 != 0):
    print('NO')
else:
    print('YES')
    list1 = []
    list2 = []
    end = n
    if n % 2 == 0:
        for i in range(1, n // 2 + 1):
            if len(list1) > len(list2):
                list2.extend([str(i), str(end)])
            else:
                list1.extend([str(i), str(end)])
            end -= 1
    else:
        end = n + 1
        for i in range(1, (n+ 1) // 2 + 1):
            if len(list1) > len(list2):
                list2.extend([str(i), str(end)])
            else:
                list1.extend([str(i), str(end)])
            end -= 1
        list1.pop(1)
        list1.append(list2[len(list2) - 2])
        list2.pop(len(list2) - 2)
 
    print(len(list1))
    print(' '.join(list1))
    print(len(list2))
    print(' '.join(list2))