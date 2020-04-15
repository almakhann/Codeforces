def q():
    n,m = [int(x) for x in input().split(' ')]
    for i in range(n):
        for j in range(9):
            if (i*2) + j == n and (i+j)%m == 0:
               
                print(i+j)
    return -1
        
            
print(q())
