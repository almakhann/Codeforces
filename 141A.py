f = input()
f = list(f + input())
n = list(input())

f.sort()
n.sort()

if f == n:
    print('YES')
else:
    print('NO')
