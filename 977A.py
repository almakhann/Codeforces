n = list(map(int,input().split()))
a = n[0]


while n[1] != 0:
    if str(a)[-1] == '0':
        a = int(a /10)
        n[1] -= 1
    else:
        a -= 1
        n[1] -= 1


print(a)
