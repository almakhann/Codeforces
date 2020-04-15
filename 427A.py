n = int(input())
m = list(map(int,input().split()))


a = 0
count = 0
for i in range(n):
    a += m[i]
    
    if a < 0:
        count+=abs(m[i])
        a = 0
        
print(count)

    
