n = int(input())
b = input()

count_a = b.count('A')
count_d = b.count('D')

if count_a > count_d:
    print('Anton')
elif count_a < count_d:
    print('Danik')
else:
    print('Friendship')
