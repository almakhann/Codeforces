##1
##a = input()
##b = input().split(' ')
##
##w = set(b)
##print(len(w))

###2
##a = int(input())
##count = 0
##while a > 0:
##    count+=1
##    a=a//2
##
##print(count)


n = int(input())
a = [int(x) for x in input().split(' ')]
tmp = []

for i in range(n):
    tmp = a[:i+1]
    tmp.sort()
    s = ""

    if i>=5:
        for j in range(5):
            s = str(tmp[j]) + " " + s
    else:
        for j in range(i+1):
            s = str(tmp[j]) + " " + s
    print(s)

for i in range(n):
    if i >= 5:
        
    
