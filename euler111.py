'''Euler problem 111
Primes with runs
I left this cranking all day and it never
came up with the 10-digits sum'''

'''From Sharas on stackoverflow
http://stackoverflow.com/questions/567222/simple-prime-generator-in-python'''

import math
import itertools
import time

t1 = time.time()

def create_prime_iterator(rfrom, rto):
    """Create iterator of prime numbers in range [rfrom, rto]"""
    prefix = [2] if rfrom < 3 and rto > 1 else [] # include 2 if it is in range separately as it is a "weird" case of even prime
    odd_rfrom = 3 if rfrom < 3 else make_odd(rfrom) # make rfrom an odd number so that  we can skip all even nubers when searching for primes, also skip 1 as a non prime odd number.
    odd_numbers = (num for num in range(odd_rfrom, rto + 1, 2))
    prime_generator = (num for num in odd_numbers if not has_odd_divisor(num))
    return itertools.chain(prefix, prime_generator)

def has_odd_divisor(num):
    """Test whether number is evenly divisable by odd divisor."""
    maxDivisor = int(math.sqrt(num))
    for divisor in range(3, maxDivisor + 1, 2):
        if num % divisor == 0:
            return True
    return False

def make_odd(number):
    """Make number odd by adding one to it if it was even, otherwise return it unchanged"""
    return number | 1

def checkDigit(num,dictA):
    '''returns max reps of every digit of num, sum of nums
    with max reps'''
    for i in range(10):
        stri = str(i)
        strnum = str(num)
        reps = strnum.count(str(i))
        try:
            dictA[i][reps].append(num)
        except KeyError:
            dictA[i][reps] = [num]
    return dictA

def S2(dPrime):
    '''returns sum of all S(n,d)'s'''
    sumA = 0
    p = create_prime_iterator(1000000000,10000000000)
    f = next(p)
    #print(f)
    dictA = {0:{},1:{},2:{},3:{},4:{},5:{},6:{},
             7:{},8:{},9:{}} #dictionary of repeated digits
    while f < 10000000000:
        dictA = checkDigit(f,dictA)
        try:
            f = next(p)
        except StopIteration:
            break
    for i in range(10):
        m = max(dictA[i])
        sumA += sum(dictA[i][m])
    print(sumA)

S2(4)

def S(dPrime,digit):
    '''returns sum of the primes with dPrime digits
    containing the max number of digit "digit"'''

    p = create_prime_iterator(1000,10000)
    f = next(p)
    #print(f)
    digitDict = dict() #dictionary of repeated digits
    while f < 10000:
        fstr = str(f)
        reps = fstr.count(str(digit))
        try:
            digitDict[reps].append(f)
        except KeyError:
            digitDict[reps] = [f]
        try:
            f = next(p)
        except StopIteration:
            break

    m = max(digitDict)
    #Worked like a charm on example table:
    #print(m,len(digitDict[m]),sum(digitDict[m]))
    return sum(digitDict[m])

'''sums = 0
for i in range(10):
    sums += S(4,i)
print(sums)'''


t2 = time.time()
print(t2-t1)
