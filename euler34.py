'''project euler problem 34
Digit Factorials'''

#from math import factorial
import time

def factorial(n):
    '''returns n!, the factorial of n'''
    if n <= 1: return 1
    else:
        return n*factorial(n-1)

now = time.time()

facts = []

for i in range(3,1000000):
    sum1 = 0
    for digit in str(i):
        sum1 += factorial(int(digit))
    if sum1 == i:
        facts.append(i)

print(facts,sum(facts))

now2 = time.time()
print(now2 - now)
