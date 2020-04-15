n = int(input())

def count_sum(t):
    sum_s = sum([int(x) for x in str(t)])
    return sum_s

a = n//2 
b = n - a


print(count_sum(a) + count_sum(b))
