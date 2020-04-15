n = list(map(int,input().split()))

t = 0
count = 1

while t == 0:
    if n[1]*count <= n[0]:
        count += 1
        n[0] += 1
    else:
        break
print(n[0])
