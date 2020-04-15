first = input().split(' ')
second = input().split(' ')

count = 0 
for i in range(int(first[0])):
    if int(second[i]) > 0:
        if int(second[i]) >= int(second[int(first[1])-1]):
            count += 1
print(count)
                             
