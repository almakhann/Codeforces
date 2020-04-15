a = input().split('+')
a.sort()
s = ''

for i in range(len(a)):
    s += a[i]+'+'

print(s[:-1])
