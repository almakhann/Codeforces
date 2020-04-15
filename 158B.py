n = input()
m = [int(x) for x in input().split(' ')]

a = [0,0,0,0,0]

if len(m) == 1:
    print(1)
else:
    for i in m:
        a[i] += 1
        
    print(a[4] + (max(a[1] - a[3],0) + a[2]*2 +3)//4 + a[3] )
