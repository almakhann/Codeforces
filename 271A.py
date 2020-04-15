a = (input())

def counter(a):
    b = ''.join(set(a))
    if len(a) == len(b):
        return a
    else:
        return False

t = 0
while t == 0:
    a = str(int(a)+1)
    result = counter(a)

    if result != False:
        print(result)
        break
