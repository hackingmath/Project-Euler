'''Project Euler problem 6
Sum Square Difference'''

import time
t1 = time.time()

def sumSquares(n):
    squares = [x**2 for x in range(1,n+1)]
    return sum(squares)

def squSums(n):
    sumOfn = sum([x for x in range(1,n+1)])
    return sumOfn**2

def euler06(n=100):
    '''for j in range(1,n + 1):
        print(j,squSums(j)-sumSquares(j))'''
    return squSums(n) - sumSquares(n)

def formula(n):
    return (3*n**4 + 2*n**3 - 3*n**2+-2*n)/12

#print(euler06(10000))
print(formula(10000))

t2 = time.time()

print(t2-t1)
