n = [int(x) for x in input().split(' ')]
m = input()

s = m

for i in range(n[0] - 1):
    if m[i] == 'B' and m[i+1] == 'G':
        s[i] = 'G'
        s[i+1] = 'B'
print(s)

