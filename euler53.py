'''Problem 53: Combinatoric selections'''

import time

t1 = time.time()

def fact(n):
    if n <= 1:
        return 1
    return n*fact(n-1)


def combinations(n,r):
    '''returns nCr'''
    return fact(n)/(fact(r)*fact(n-r))

tot = 0

for n in range(1,101):
    for r in range(1,101):
        if combinations(n,r)>1000000:
            tot += 1

print(tot)

t2 = time.time()

print(t2-t1)

#4075 Correct in 0.34 seconds
