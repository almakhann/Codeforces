n = list(map(int,input().split()))

t = 0
count = 1
while t == 0:
    if ((count*n[0]) % 10) == 0 or (((count*n[0]) - n[1]) % 10) == 0:
        break
    else:
        count += 1
print(count)
