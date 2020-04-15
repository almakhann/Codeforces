n = int(input())

t = 0
l = []

while t < (n+5):
    if t <= 1:
        l.append(t)
    else:
        l.append(l[-1] + l[-2])
    t+=1

st = ''
for i in range(1,n+1):
    if i in l:
      
        st+='O'
    else:
        st+='o'

print(st)
        
