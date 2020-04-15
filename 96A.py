a = input()

count = 0
count1 = 0
yes = 0

for i in range(len(a)):
    if a[i] == '0':
        count+=1
        count1 = 0
    else:
        count1+=1
        count = 0

    if(count>=7 or count1>=7):
        print('YES')
        yes = 1
        break


if(yes == 0):
    print('NO')
