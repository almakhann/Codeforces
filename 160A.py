a = input()
b = [int(x) for x in input().split(' ')]

count = 0
c = 0
b.sort()

t = 0

while t == 0:
    if count <= sum(b):
        count += b[-1]
        c += 1
        del b[-1]
    else:
        break

print(c)
