n = int(input())
m = [int(x) for x in input().split(' ')]

if len(m) > 1:
    max_s = max(m)
    count = 0
    for i in range(n):
        count += max_s - m[i]
else:
    count = 0

print(count)
