
l = []
for i in range(5):
    a = input().split(' ')
    l.append(a)


for i in range(5):
    for j in range(5):
        if(l[i][j] == '1'):
            print(abs(i-2) + abs(j-2))
