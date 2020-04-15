a = input()

l = []
for i in range(int(a)):
    b =[int(x) for x in input().split(' ')]
    l.append(b)



l2 = []
count = 0
for i in range(int(a)):
    for j in range(2):
        if j == 0:
            count -= l[i][j]
        else:
            count += l[i][j]
    l2.append(count)

print(max(l2))
