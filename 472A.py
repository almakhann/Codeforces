n = int(input())

def fib(n):
    dic = {}
    for i in range(1,n+1):
        if i <= 2:
            dic[i] = 1
        else:
            dic[i] = (dic.get(i-1) + dic.get(i-2))
    return dic.get(n)
print(fib(n))
