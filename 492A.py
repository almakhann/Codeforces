n = int(input())

m = 0
count = 1
total = 0
while total < n:
    count+=1
    m += count
    total += m
    

    
print(count-1 if total > n else count)
   
    

