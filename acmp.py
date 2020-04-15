##
##
##first = input()
##second = input().split(' ')
##
##pos = 0
##
##max_n = -1
##min_n = 9999999
##
##for i in range(int(first)):
##    if int(second[i]) > 0:
##        pos += int(second[i])
##
##    if max_n < int(second[i]):
##        max_n = int(second[i])
##    if min_n > int(second[i]):
##        min_n = int(second[i])
##    
##
##p = second.index(str(max_n))
##n = second.index(str(min_n))
##
##def prod(less,maxx):
##    count = 1
##    for i in second[less+1:maxx]:
##        count = count * int(i)
##    return count
##
##if (n>p):
##    print(pos,prod(p,n))
##else:
##    print(pos,prod(n,p))
##
##
##
##

a = input()

first = []
count = 1
for i in range(int(a)):
    second = []

    for j in range(i+1):
        second.append(count)
        count += 2
    first.append(second)

sum_s = sum(first[int(a)-1]) 
print(sum_s)



