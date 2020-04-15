a = list(map(int, input().split()))

count = 0
t = 0
while t == 0:
    if a[0] != 0 and a[1] != 0:
        a[0] -= 1
        a[1] -= 1
        count += 1
    else:
        break

if count % 2 == 0 :
    print('Malvika')
else:
    print('Akshat')
