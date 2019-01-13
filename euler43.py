'''Project Euler problem 43
Sub-string divisibility
solved 4/22/16

Adapted the pandigital code from problem 41'''

import time
from itertools import permutations
from math import sqrt

t1 = time.time()

def isPandigital(n):
    '''returns True if n contains all the digits 1-9'''
    strn = str(n) #convert to string
    if len(strn) != 9: return False
    if not isPrime(n):return False
    for i in range(1,10):
        if strn.count(str(i)) != 1:
            return False
    return True

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def pandigitList():
    #create list of 9-digit pandigitals:
    pandigitals = []
    pans = permutations('1234567890')
    
    while True:
        try:
            p = next(pans)
            #print(p)
            n = '' #make string of list of digits
            for x in p:
                n += x
            n = int(n)
            pandigitals.append(n)

        except StopIteration:
            break
    return pandigitals

def divisibility(n):
    '''Returns True if pandigital's sub-strings
    are divisible by the primes'''
    prime = [2,3,5,7,11,13,17]
    strn = str(n)
    for i,v in enumerate(prime):
        div = strn[i+1:i+4]
        #print("div,v: ",div,v)
        if int(div) % v != 0:
            return False
    return True

pandigitals = pandigitList()
print("ex?",1406357289 in pandigitals)

panSum = 0
for p in pandigitals:
    if divisibility(p):
        print(p)
        panSum += p

print("sum: ",panSum) # correct answer: 16695334890

t2 = time.time()

print(t2 - t1)
