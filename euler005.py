'''Euler problem 5: Smallest Multiple'''

from itertools import combinations
from math import factorial,sqrt

#from lassevk on PE forum. very fast:
'''i = 1
for k in (range(1, 101)):
    if i % k > 0:
        for j in range(1, 101):
            if (i*j) % k == 0:
                i *= j
                break
print (i)'''

def eratsieve(num):
    #creates a list of primes up to n using Eratosthenes' sieve
    #first create a list of all the numbers up to num
    list1 = [n for n in range(2,num)]
    #now change all the multiples of each number to 1
    for i in range(2,int(sqrt(num))):
        if i in list1:
            for v,j in enumerate(list1):
                if type(j) == int and j % i == 0  and j > i:
                    list1[v] = 'X'
    primes = [x for x in list1 if x != 'X']
    return primes

primes = eratsieve(100)

def factors(n):
    '''returns a list of prime factors of n'''
    factorList = list()
    while n not in primes:
        for prime in primes:
            if n % prime == 0:
                factorList.append(prime)
                n = int(n/prime)
                if n == 1:
                    break
    factorList.append(n)
    factorList.sort()
    return factorList

#print(factors(12))

def lcm(a,b):
    '''returns the lowest common multiple of a and b'''
    lcm = 1
    afacts = factors(a)
    bfacts = factors(b)
    print(afacts, bfacts)
    combfacts = set(afacts + bfacts)
    print(combfacts)
    for prime in combfacts:
        #count number of times prime appears in factors
        if prime in afacts and prime in bfacts:
            times = max(afacts.count(prime),bfacts.count(prime))
        elif prime in afacts:
            times = afacts.count(prime)
        else:
            times = bfacts.count(prime)
        lcm *= prime ** times
    return lcm

'''n = 20



numList = range(1,n+1)
primeList = eratsieve(n)

strPrimeList = [1]+[str(x) for x in primeList]
strList = [str(x) for x in numList]

#print(strList)

factors = combinations(strPrimeList,2)

nums = []
while True:
    try:
        f = next(factors)
    except StopIteration:
        break
    nums.append(int(f[0])*int(f[1]))

nums.sort()
print(nums)'''
