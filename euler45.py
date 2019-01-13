'''Project Euler
problem 45: Triangular, pentagonal and hexagonal'''

import time
from math import sqrt

t1 = time.time()

triangs = []
pents = []
hexags = []

def old():
    for n in range(1,100000):
        #triangs.append(n*(n+1)/2)
        pents.append(n*(3*n-1)/2)
        hexags.append(n*(2*n-1))

    for h in hexags:
        if h in pents:
            t2 = time.time()
            print(h,t2 - t1)

'''Results:
1 0.09663271903991699
40755 1.059443473815918
1533776805 235.2919898033142
#somebody in the forum pointed out that all hexagonal
#numbers are also triangular numbers! I took out
the check for triangs and the new times:
1 0.06005072593688965
40755 1.05902099609375
1533776805 183.50306868553162'''

#This was off the forum:
n=1
t1 = time.time()
while True:
    n += 1
    h = n*(2*n-1)
    k = (1+sqrt(1+24*h))/6
    if k == int(k):
        t2 = time.time()
        print(h,t2 - t1)

#It got the answer in a fraction of a second: 0.05056619644165039
