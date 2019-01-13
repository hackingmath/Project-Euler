'''Project Euler Problem 72
Counting fractions'''

import time
from urllib.request import urlopen
from fractions import Fraction

now = time.time()

def factors(n):
    '''returns a set of all the factors of n'''
    return [x for x in range(1,n+1) if n%x==0]

def propFracs(n,d):
    '''returns set of all fractions n / d'''
    return {Fraction(i,j) for i in factors(n) for j in factors(d) if i<j}

def allFracs():
    a= set()
    for n in range(1,1000000):
        for d in range(1,1000001):
            for frac in propFracs(n,d):
                a.add(frac)
    return a

print(allFracs())
print(len(allFracs()))

then = time.time()
elapsed = then - now
print(elapsed)

# got correct answer on test (d<=8) in 0.07 sec

