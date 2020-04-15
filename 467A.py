n = input()
m = [[int(x) for x in input().split(' ')]for i in range(int(n))]


count = 0
for i in range(int(n)):
    if m[i][1] - m[i][0] >= 2:
        count += 1
print(count)
