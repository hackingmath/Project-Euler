'''Project Euler problem 41
Pandigital prime
4/22/16

Adapted the pandigital code from problem 38'''

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
    for i in range(9,5,-1): #use first i digits
        nums = ''
        for j in range(1,i+1):
            nums += str(j)
        pans = permutations(nums,i)
        
        while True:
            try:
                p = next(pans)
                #print(p)
                n = '' #make string of list of digits
                for x in p:
                    n += x
                n = int(n)
                if isPrime(n):
                    pandigitals.append(n)

            except StopIteration:
                break
    #print(pandigitals[:10])
    return pandigitals

pandigitals = pandigitList()

print("pandigital list done. Length:",len(pandigitals))

print(max(pandigitals)) #correct answer: 7652413 in 1 sec
t2 = time.time()

print(t2 - t1)
