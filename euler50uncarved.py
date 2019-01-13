'''Euler Problem 50 by uncarvedblock'''
import time

t1 = time.time()

def primesieve(bound):
    A = [0]*bound
    for i in range(2,bound):
        if A[i] == 0:
            for k in range(2, -(-bound // i)):
                A[i*k] += 1
    return [p for p in range(2,bound) if A[p] == 0]

def isprime(n, primes = None):
    if not primes: primes = primesieve(int(n**0.5) + 1)
    for p in primes:
        if n % p == 0:
            return False
    return True

def main():
    primes = primesieve(5*10**3)
    i, j = 0, 0
    total = 0
    # find indices summing to > 1 million with i = 0
    while total < 10**6:
        total += primes[j]
        j += 1
    # find indices summing to prime less than 1 million with i = 0
    while not isprime(total, primes):
        j -= 1
        total -= primes[j]
    consecutive = j - i
    best = (i, j) # endpt j not included
    # keep increasing i and trying to find a longer sequence, until not possible
    while sum(primes[i:(i + consecutive)]) < 10**6:
        i += 1
        j = i + consecutive
        while sum(primes[i:j]) < 10**6:
            j += 1
            if isprime(sum(primes[i:j]), primes):
                best = (i, j)
                consecutive = j - i
    i, j = best
    summation = sum(primes[i:j])
    print("sum of {} consecutive primes from {} to {} equals {}".format(consecutive, \
        primes[i], primes[j-1], summation))

main()
t2 = time.time()

print("time: ",t2-t1)
