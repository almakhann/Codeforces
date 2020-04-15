a = int(input())
n = list(input())
m = list(input())

count = 0
for i in range(a):
    count += min(abs(int(n[i]) - int(m[i])), 10 - abs(int(n[i]) - int(m[i])))
print(count)
