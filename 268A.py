n = int(input())

m = []
for i in range(n):
    m.append(list(map(int,input().split())))

count = 0
for i in range(n):
    for j in range(n):
        if i != j and m[i][0] == m[j][1]:
            count += 1
print(count)
