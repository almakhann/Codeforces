n = int(input())
m = [int(x) for x in input().split(' ')]

m.sort()

count = 0
for i in range(n):
    if i != n/2:
        a = 0
        a = (m[i] + m[(n-i)-1]) **2
        count += a
    else:
        break
print(count)
