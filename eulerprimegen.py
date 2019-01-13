'''Problem 47
Distinct primes factors'''

from primeSharas import create_prime_iterator
import time

t1 = time.time()

primes = list(create_prime_iterator(1,100000))

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

#fourPs()
#no solution in first 100,000: took 547.1 sec so far
#134043 [3, 7, 13, 491] 134044 [2, 23, 31, 47] 134045 [5, 17, 19, 83] 134046 [2, 3, 11, 677]
#469.017361164093 sec

'''This was suggested by Brian on PE forum. It returned the answer in less
than a second.'''

Limit=1000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in range(2,Limit): #from 2 to a million
    print(factors)
    if factors[i]==0:   #if the entry is 0
        # i is prime
        count =0 
        val =i
        while val < Limit:
            factors[val] += 1 #increase the factors of val
            val+=i          #increase all the factors of i
    elif factors[i] == 4:
        count +=1
        if count == 4:
            print(i-3) # First number
            break
    else:
        count = 0

t2 = time.time()
print(t2 - t1)
