'''Project Euler problem 35
Circular Primes
1/4/16
correct answer: 55'''
from math import sqrt
import time

def isPrime(n):
    '''returns True if n is Prime'''
    for i in range(2,int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def rotation(n):
    b = str(n)
    rlist = []
    for i in range(len(b)):
        rlist.append(int(b))
        b = b[1:]+b[0]
    return rlist

def circular(n):

    for i in rotation(n):
        if not isPrime(i):
            return False
    return True
now = time.time()
count = 0
for i in range(2,1000001):
    if circular(i):
        count += 1
print(count)
now2 = time.time()
print(now2 - now)
