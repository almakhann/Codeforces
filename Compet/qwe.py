m = int(input())

l=[]
for i in range(m):
    n = input()
    l.append(n)

count = 0
for i in range(m-1):
    for j in range(1,m-1):
        if l[i-1][j-1] == 'X' and l[i-1][j+1] == 'X' and  l[i+1][j-1] == 'X' and l[i+1][j+1] == 'X':
            count += 1
print(count)
