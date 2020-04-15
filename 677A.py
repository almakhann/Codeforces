n = [int(x) for x in input().split(' ')]
m = list(map(int,input().split()))

count = 0
for i in range(n[0]):
    if m[i] <= n[1]:
        count += 1
    else:
        count += 2
print(count)
