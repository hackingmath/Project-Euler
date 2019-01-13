'''Problem 57: square root convergents'''

import time
from fractions import Fraction
from decimal import Decimal

t1 = time.time()

tot = 0

def f(level):
    if level == 0:
        return 2
    return 2 + 1/f(level-1)

for i in range(10):
    g =  (1 + 1/f(i))
    print(g,Fraction(Decimal(str(g))))

t2 = time.time()

print(t2-t1)

#Correct Answer: 972 in 0.3 seconds
