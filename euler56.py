'''Problem 56: Powerful digit sum'''

import time

t1 = time.time()

tot = 0

def digSum(n):
    '''returns sum of digits of n'''
    a = [int(x) for x in list(str(n))]
    return sum(a)

for a in range(1,101):
    for b in range(1,101):
        p = digSum(a**b)
        if p > tot:
            tot = p

print(tot)

t2 = time.time()

print(t2-t1)

#Correct Answer: 972 in 0.3 seconds
