n = int(input())

result = ''
for i in range(1,n+1):
    if i%2 == 1 :
        if n != 1 and i != n:
            result += 'I hate that '
        else:
            result += 'I hate it '
    else:
        if i != 1 and i != n:
            result += 'I love that '
        else:
            result += 'I love it '
print(result)
