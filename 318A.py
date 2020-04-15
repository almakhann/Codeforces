n = list(map(int,input().split()))

l = []
if n[0] / 2.0 >= n[1]-0.5:
    print(2*n[1]-1)
else:
    if n[0] % 2 == 0:
        print((n[1] - n[0]//2) * 2)
    else:
        print((n[1]- n[0]//2 -1) * 2)

