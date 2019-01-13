'''Problem 52 Permuted multiples'''
import time

t1 = time.time()

def digits(num):
    '''returns true if 2*x,3*x,4*x,5*x and 6*x
    all have the same digits'''
    a = set()
    b = set()
    c = set()
    d = set()
    e = set()

    for digit in str(2*num):
        a.add(digit)

    for digit in str(3*num):
        b.add(digit)

    for digit in str(4*num):
        c.add(digit)

    for digit in str(5*num):
        d.add(digit)

    for digit in str(6*num):
        e.add(digit)

        
    return a==b==c==d==e

for i in range(100000,1000000):
    if digits(i):
        print(i)
        break

t2 = time.time()
print(t2-t1)
    
#Answer 142857 in .3 seconds
