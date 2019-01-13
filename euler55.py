'''Problem 55: Lychrel numbers'''

import time

t1 = time.time()

tot = 0

def palin(n):
    '''returns True if n is a palindrome'''
    return str(n) == str(n)[::-1]

def revAndAdd(n):
    '''reverses a numbers digits and adds
    the two numbers'''
    return n + int(str(n)[::-1])

def lychrel(n):
    '''returns true if n is Lychrel num'''
    for i in range(50):
        n = revAndAdd(n)
        if palin(n):
            return False
    return True

for i in range(10,10000):
    if i % 1000 == 0:
        print("Testing",i)
    if lychrel(i):
        tot += 1

print(tot)

t2 = time.time()

print(t2-t1)

'''Correct answer: 249
0.15022563934326172 seconds'''
