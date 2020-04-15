n = list(map(int,input().split()))
n.sort()

count = (n[1] - n[0]) + (n[2] - n[1])
print(count)
