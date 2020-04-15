n = list(map(int,input().split()))


if n[0] >= n[1]:
    diff = n[1]
else:
    diff = n[0]

same = int(abs(n[0]-n[1]) /2)

print(diff, same)
