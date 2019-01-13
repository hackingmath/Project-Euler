'''Problem 41
Pandigital Prime
'''

from primeSharas import create_prime_iterator
import time
from itertools import permutations
from math import sqrt

t1 = time.time()

primes = list(create_prime_iterator(1000,10000))
pgen = create_prime_iterator(1000,10000)

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def perms1(n):
    pstr = str(n)
    prime_perms = set()
    perms = permutations(pstr)
    while True:
        try:
            b = next(perms) #list of string objects
            #print(b)
            c = ''
            #This will make the permutation a string
            for i in range(4):
                c += b[i] 
            #print("c = ",int(c))
            #print("isPrime(c)?",isPrime(int(c)))
            if isPrime(int(c)):
                prime_perms.add(int(c))
            pp = list(prime_perms)
            
        except StopIteration: #when permutations run out
            #print(b)
            break
    #print("pp:",pp)
    if len(pp) < 3:
        return False
    pp.sort()
    #print("sorted",pp)
    gen = permutations(pp,3)
    while True:
        
        try:
            g = next(gen)
            #print("perms:",g)
            if g[1]-g[0] == g[2]-g[1]:
                print(g)
                return True
        except StopIteration: #when permutations run out
                #print(b)
                break

    return False

        
for prime in primes:
    if perms1(prime):
        print(prime)

#tested the example on PE: print(perms1(1487))


def factors(n):
    '''List of factors of n'''
    return [i for i in range(2,n) if n % i == 0]

def pfactors(n):
    '''List of prime factors of n'''
    return [i for i in range(2,n) if n % i == 0 if i in primes]

def threePs():
    '''test for 3 consecutives with
    three pfactors'''
    for i in range(2,1000):
        if len(pfactors(i)) == 3 and \
           len(pfactors(i+1)) == 3 and \
           len(pfactors(i+2)) == 3:
            print(i,pfactors(i),i+1,pfactors(i+1),i+2,pfactors(i+2))
            return

#worked perfectly: 644 [2, 7, 23] 645 [3, 5, 43] 646 [2, 17, 19]

def fourPs():
    '''test for 3 consecutives with
    three pfactors'''
    for i in range(100000,200000):
        if i %1000 == 0: print(i) #print out the progress
        if len(pfactors(i)) == 4:
            if len(pfactors(i+1)) == 4 and \
               len(pfactors(i+2)) == 4 and \
               len(pfactors(i+3)) == 4:
                    print(i,pfactors(i),
                      i+1,pfactors(i+1),
                      i+2,pfactors(i+2),
                      i+3,pfactors(i+3))
                    return


t2 = time.time()
print(t2 - t1)
