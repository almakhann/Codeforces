n = [int(x) for x in input().split(' ')]

count = 1
for i in range(n[0]):
    if i % 2 == 1:
        if count % 2 ==1: 
            print('.'*(n[1]-1)+'#')
        else:
            print('#'+'.'*(n[1]-1))
        count+=1
    else:
        print('#'*n[1])
