n = input()

up_c = 0
low_c = 0
for i in n:
    if i.islower():
        low_c += 1
    else:
        up_c += 1

if up_c <= low_c:
    print(n.lower())

else:
    print(n.upper())
