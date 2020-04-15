n = input()
m =[[int(x) for x in input().split(' ')]for i in range(int(n))]

print(m)


l = []
for i in range(3):
    l = []
    for j in range(int(n)):
        l.append(m[j][i])
    if sum(l) != 0:
        print('NO')
        exit()


print('YES')

