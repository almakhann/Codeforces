a = [int(x) for x in input().split(' ')]

count = 0
for i in range(1,a[2]+1):    
    count += a[0]*i

if count > a[1]:
    print(count-a[1])
else:
    print(0)
