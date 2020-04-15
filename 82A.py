import math

d = {1:"Sheldon",2: "Leonard",3: "Penny",4: "Rajesh",5: "Howard" }

n = int(input())

t = 0
exp = 0
while n > exp:
    exp += 5*(2**t)
    t += 1

last = 0
for i in range(t-1):    
    last += 5*(2**i)

exp = n - last
res = math.ceil(exp/2**(t-1))


print(d.get(res))
