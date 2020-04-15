n = list(map(int,input().split()))
m = list(map(int,input().split()))

sum_m = sum(m)
if n[1] == (sum_m + n[0]-1):
    print('YES')
else:
    print('NO')
