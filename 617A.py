a = int(input())

count = 0
t = 0
while t < a:
    for i in reversed(range(1,6)):
       
        count += 1
        t += i
        break
    
print(count)
