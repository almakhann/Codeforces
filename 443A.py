import re


a = input()
a = a[1:len(a)-1].split(',')


m = []
for i in a:
    if i.strip() not in m and i != '':
        m.append(i.strip())

print(len(m))
