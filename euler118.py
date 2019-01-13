'''Project Euler problem 118
Pandigital prime sets'''

import time
import json

def isPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

def fillPrimeList(maxi=1000000):
    '''returns a list of primes up to maxi'''
    f=open('primelist.txt','w')
    primes = [2]
    f.write('2,')
    for i in range(3,maxi + 1):
        prime = True
        for prime in primes:
            if i % prime == 0:
                prime = False
                break
        if prime:
            f.write(str(i)+',')
            primes.append(i)
    f.close()

now = time.time()
def createPrimeList():
    '''creates a .txt file containing
    a list of primes'''
    f = open('testprimelist.txt','w')
    plist = primeList(1000)
    json.dump(plist,f)
    f.close()

#fillPrimeList()

def addToPrimeList():
    f = open('primelist.txt','r')
    j = f.read()
    if j[-1] == ',': j = j[:-1]
    k = [int(s) for s in j.split(',')]
    f.close()
    f = open('primelist.txt','a')
    for i in range(1000001,10000000001):
        prime = True
        for prime in k:
            if i % prime == 0:
                prime = False
                break
        if prime:
            f.write(str(i)+',')
            k.append(i)
    f.close()

def reducePrimeList():
    '''creates list of prime numbers with
    no repeated digits.'''
    f = open('primelist.txt','r')
    j = f.read()
    if j[-1] == ',': j = j[:-1]
    k = [int(s) for s in j.split(',')]
    f.close()

    #print(k)

    g = open('primenorptlist.txt','w')

    plist2 = []
    for prime in k:
        only1 = True
        pstr = str(prime)
        for digit in pstr:
            if pstr.count(digit) != 1:
                only1 = False
                break
        if only1:
            plist2.append(prime)

    json.dump(plist2,g)
    g.close()

#now plist2 has all the primes with no repeated numbers
#reducePrimeList()
#print(len(plist2))
addToPrimeList()
then = time.time()
print(then-now)
