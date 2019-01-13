'''Project Euler problem 50
Consecutive Prime Sum
4/22/16
'''
import time
from math import sqrt

t1 = time.time()

def isPrime(n):
    for i in range(2,int(sqrt(n))+1):
        if n%i == 0:
            return False
    return True

file = open('primes1.txt')

primes = []

for num in file.read().split():
    num = int(num)
    if num < 10000:
        primes.append(num)
    else:
        break

file.close()

#print(len(primes)) #78498 primes
length = len(primes)
primeRuns = {} #have to populate the dictionary first

for i,p in enumerate(primes):
    prime = False
    j = 0 # number of terms from the end of the primes list
    while not prime:
        runSum = sum(primes[i:length-j]) #sum up a slice
        if runSum < 1000000 and isPrime(runSum):
            prime = True
            this_run = length - j - i
            primeRuns[this_run] = runSum #add to dictionary
        j += 1 #if not prime, sum up one less term
        if i == length - j: #if the slice is empty
            break 
    
'''for i,p in enumerate(primes):
    maxRun = 0
    maxRunSum = 0
    this_run = 0
    #print(i,p)
    runSum = 0 #runsum starts at the prime
    while runSum < 1000:
        runSum += primes[this_run]
        this_run += 1
        if runSum in primes:
            #print(runSum)
            primeRuns[runSum] = this_run
            if maxRunSum < runSum:
                maxRunSum = runSum
            if maxRun < this_run:
                maxRun = this_run
    #print("max: ",maxRunSum,"maxRun: ",maxRun)'''

'''for k in range(70000): #go through 10000 primes
    for i in range(17,25): #try sums from 17 to 24 primes long
        runSum = primes[k:k+i] #the sum of i primes
        if sum(runSum) in primes: #if the sum is prime
            primeRuns[sum(runSum)] = runSum #add it to the primeRuns dictionary'''

#maxRun = max(primeRuns.keys(), key=(lambda k: len(primeRuns[k])))
print ("Final max: ",max(primeRuns), primeRuns[max(primeRuns)])

t2 = time.time()

print(t2 - t1)

'''At first I tried to add a bunch of prime numbers together:
197 12-run, not the solution.
876041 15-run, not the solution.
176129, a 17-run, is not the solution
Then I switched to adding consecutive primes together like crazy and
checking for prime-ness. The max so far is 958,577, the sum of 536 primes,
but PE says it isn't the solution! It cranks through for an hour before i give up.
Tried slicing the primes list instead.
Tested it successfully on the example under 1,000 so tried it on a million.
Final max: 997651 is the sum of 543 consecutive primes!
solution in 2.9 seconds
'''

