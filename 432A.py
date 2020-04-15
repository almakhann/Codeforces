a,b = list(map(int,input().split()))
m = [int(x) for x in input().split(' ')]

count = 0
for i in range(a):
    if (m[i] + b) <= 5:
        count+=1


print(count//3)
    
