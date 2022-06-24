import math

t = [0.0, 5.0, 10., 20., 30., 40., ]
u = [1.787, 1.519, 1.307, 1.002, 0.797, 0.653]
jx = 0
jlny = 0
jxlny = 0
jx2 = 0
n = len(t)

for i in range(n):
    jx = jx + math.log(t[i],2 )
    jlny = jlny + math.log(u[i], 2)
    jxlny = jxlny + math.log(u[i], 2 ) * t[i]
    jx2 = jx2 + t[i]*t[i]
a1 = (n*jxlny-jlny*jx)/(n*jx2 - (jx)**2)
lnd = 1/n*(jlny-a1*jx)
print(lnd)
print("nilai B adalah = %0.5f" %a1 + "dan nilai D adalah =  %0.5f " %lnd)


