n = int(input())
m = list(map(int,input().split()))

count = 0
for i in m:
    if i%2 == 0:
        count += 1

if count == 1:
    for i in m:
        if i%2 == 0:
            print(m.index(i) + 1)
            break
else:
    for i in m:
        if i%2 != 0:
            print(m.index(i) + 1)
            break
