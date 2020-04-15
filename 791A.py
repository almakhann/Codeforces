n = list(map(int,input().split()))

t = 0
count = 1
while t == 0:
    n[0] = n[0] * 3
    n[1] = n[1] * 2
    if n[0] > n[1]:
        break
    count += 1

print(count)
