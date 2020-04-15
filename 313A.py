n = int(input())

a= ''
if n >= 0:
    print(n)
else:
    if str(n)[-1] >= str(n)[-2]:
        a = str(n)[:-1]
    else:
        a = str(n)[:-2]+str(n)[-1]
    print(int(a))
    
