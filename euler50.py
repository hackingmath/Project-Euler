'''Problem 50
consecutive prime sum'''

from primeSharas import create_prime_iterator
import time

t1 = time.time()

primes = list(create_prime_iterator(1,100000))

i = 0
max = 0

for i in range(len(primes)):
    count = 0
    for j in primes[:i]:
        sum1 = sum(primes[i:i+count])
        if sum1 in primes and sum1 > max:
            max = sum1
            count += 1
             
print(max)
t2 = time.time()
print(t2 - t1)
