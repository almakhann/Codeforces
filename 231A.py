n = input()

l = []
count = 0

def qwe(q):
    b = 0
    for i in q:
        b += int(i)
    return b

for i in range(int(n)):
    b = input().split(' ')
    l.append(b)


for i in range(int(n)):
    a = qwe(l[i])
    if a > 1:
        count += 1

print(count)




