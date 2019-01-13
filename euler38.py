'''Project Euler problem 38
Pandigital multiples
4/12/16

I noticed the integer factor we're looking
for is the first few digits of the
pandigital, since the first number it's
multiplied by is 1.'''

import time
from itertools import permutations

t1 = time.time()

def isPandigital(n):
    '''returns True if n contains all the digits 1-9'''
    strn = str(n) #convert to string
    if len(strn) != 9: return False
    for i in range(1,10):
        if strn.count(str(i)) != 1:
            return False
    return True

def pandigitList():
    #create list of 9-digit pandigitals:
    pans = permutations('123456789')
    pandigitals = []
        
    while True:
        try:
            p = next(pans)
            n = '' #make string of list of digits
            for x in p:
                n += x
            n = int(n)
            #print(n)
            pandigitals.append(n)

        except StopIteration:
            break
    return pandigitals

pandigitals = pandigitList()

print("pandigital list done. Length:",len(pandigitals))
for i in pandigitals:
    stri = str(i) #turn number into string
    for j in range(1,6):
        divisor = stri[:j]
        numi = ''
        for k in range(1,10):
            numi += str(int(divisor)*k)
            if i == int(numi):
                print(i,divisor)
                break

t2 = time.time()

print(t2 - t1)
