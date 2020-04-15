n = list(map(int,input().split()))
l= []
for i in range(n[1]):
    l.append(list(map(int,input().split())))
l.sort()


for i in range(n[1]):
    if n[0] > l[i][0]:
        n[0] += l[i][1]
    else:
        break

if n[0] > l[n[1]-1][0]:
    print('YES')
else:
    print('NO')
