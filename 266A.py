n = input()
m = input()

count = 0

t = 0


while t == 0:
    exists = 1
    if len(m) == 1:
        break
    for i in range(len(m)-1):
        if m[i] == m[i+1]:
            m = m[:i] + m[i+1:]
            count +=1
            exists = 0
            break
    if exists == 1:
        break

print(count)

            
        
