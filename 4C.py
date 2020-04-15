from collections import Counter
n = int(input())

l=[]
q = []
for i in range(n):
    a = input()
    
    count = l.count(a)
    q.append(a+str(count)) if count>0 else q.append('OK')

    l.append(a)
        


print('\n'.join(q))
