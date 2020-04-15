a = input()

count1 = 0
count2 = 0
for i in a:
    if i == 'a':
        count1+=1

if count1 >= (len(a)/2+1) :
    print(len(a))
else:
    print(2*count1 -1)
