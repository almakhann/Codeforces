n = int(input())
m = list(map(int,input().split()))

count = 1
l = []
for i in range(n-1):
    if m[i] <= m[i+1]:
        count += 1
    else:
        l.append(count)  
        count = 1

if len(l) != 0 and max(l)> count:
    print(max(l))
else:
    print(count)

