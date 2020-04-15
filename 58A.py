a = input()

text = 'hello'

j = 0
count = 0
for i in range(len(a)):
    if a[i] == text[j]:
        count+=1
        j+=1

        if(count == 5):
            print('YES')
            break
if count != 5:        
    print('NO')
        




