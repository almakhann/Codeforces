n = [int(x) for x in input().split(' ')]
a = 240 - n[1]

t = 0
while a >= 0:
    t += 1
    a -= t*5
    if a < 0:
        t -= 1
        break
    if t == n[0]:
        break
    

print(t)
