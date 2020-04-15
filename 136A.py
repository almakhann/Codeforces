a = int(input())
m = list(map(int,input().split()))


for i in range(1,a+1):
    print((m.index(i) + 1), end=' ')


