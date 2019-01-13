'''Problem 46: Goldbach's other conjecture'''

from math import sqrt
import time

t1 = time.time()

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

primes = [j for j in range(2,10000) if isPrime(j)]

def comp(n):
    primes2 = [k for k in primes if k < n]
    x = 1
    while x < len(primes2):
        diff = n - primes2[-x]
        for i in range(1,diff+1):
            if diff == 2*i**2:
                return True
        x += 1
    return False
            
compNums = [m for m in range(3,10000) if not isPrime(m) if m % 2 == 1]

print(compNums)

for n in compNums:
    if not comp(n):
        print(n)
        t2 = time.time()
        print(t2-t1)

#answer: 5777 in 3.9 sec
