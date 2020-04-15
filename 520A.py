n = int(input())
m = input()

text = 'abcdefghijklmnopqrstuvwxyz'
if n >= 26:
    l = [] 
    for i in m.lower():
        if i in text:
            l.append(i)
    if len(set(l)) == 26:
        print('YES')
    else:
        print('NO')
else:
    print('NO')
