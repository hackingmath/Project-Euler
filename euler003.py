'''Highest prime factor'''

from math import sqrt

import time

start = time.time()

def isPrime(num):
    '''Returns True if num is Prime'''
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3,int(sqrt(num))+1,2):
        if num % i == 0:
            return False
    return True

def highest_prime_factor(num=600851475143):
    for i in range(2,int(num/2)):
        if num % i == 0:
            other_factor = int(num / i)
            if isPrime(other_factor):
                return other_factor

print(highest_prime_factor())

print("Time:",time.time()-start)
