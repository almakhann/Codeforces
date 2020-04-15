n, m = list(map(int,input().split()))
text = list(input())


while m > 0:
    i = 0
    while  i < n-1 :
        if text[i] == 'B' and text[i+1] == 'G':
            text[i] = 'G'
            text[i+1] = 'B'
            i+=1
        i+=1
    m-=1

print(''.join(text))
            
