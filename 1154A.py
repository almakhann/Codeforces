n = list(map(int,input().split()))


a = 0
j = 0
for i in range(3):
    if (n[3] - n[i]) >= 0:
        a = n[3] - n[i]
        j = i

for i in range(2):
    if i != j and (n[i]-a) >=0 and (n[i+1]-a) >= 0:
        b = n[i]-a
        c = n[i+1]-a


print(a,b,c)
 
