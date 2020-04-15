n = input()

count = 0
for i in range(int(n)):
    q = input()
    if '++' in q:
        count += 1
    else:
        count -= 1

print(count)
