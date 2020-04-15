l = []
m = []
for i in range(5):
    l.append(int(input()))

for j in range(4):
    for i in range(l[j],l[4]+1,l[j]):
            m.append(i)
    

print(len(set(m)))

