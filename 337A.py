n = list(map(int,input().split()))
m = list(map(int,input().split()))

m.sort()

min_i = 9999999999999999
for i in range(n[1] - n[0]+1):
    min_i = min(min_i,m[i+n[0]-1]- m[i])

print(min_i)

  

