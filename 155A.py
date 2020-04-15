n = int(input())
m = list(map(int,input().split()))

l = []
count = 0

l.append(m[0])
for i in range(1,n):
    if (max(l) < m[i] or min(l) > m[i]):
        l.append(m[i])
        count += 1

print(count)
