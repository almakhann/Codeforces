l = []
for i in range(int(input())):
    l.append(input())

count = 1
for j in range(len(l)-1):
    if l[j][1] == l[j+1][0]:
        count += 1
print(count)
