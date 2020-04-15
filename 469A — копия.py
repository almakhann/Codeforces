n = int(input())
m = input().split(' ')[1:]
q = input().split(' ')[1:]

final_l = set(list(set(m) | set(q)))
final_l.remove('0') if '0' in final_l else final_l



if n == len(final_l):
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
