n,m = list(map(int,input().split()))

l = []


for i in range(1,10):
    for j in reversed(range(1,10)):
        if i+j == m:
            l.append(str(i)+str(j))

        
print(l[0],l[-1] if len(l) > 1 else '-1 -1' )
