n = int(input())

def Counter(n):
    a = (sum([int(x) for x in str(n)]))
    return a

t=n
count = 0
while t > 9:
    t = Counter(t)
    count += 1

    
print(count)
