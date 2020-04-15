a = input()

count = 0
for i in a:
    if i == '4' or i == '7' :
        count+=1
    
if int(a) % 4 == 0 or int(a) % 7 == 0 or len(a) == count or  int(a) % 74 == 0 or int(a) % 47 == 0 :
    print('YES')
else:
    print('NO')
