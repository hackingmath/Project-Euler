'''Project Euler Problem 25
1000-digit Fibonacci'''

import time

def fibo(n):
    '''returns the nth Fibonacci number'''
    if n == 0 or n == 1:
        return 1
    else: return fibo(n-1) + fibo(n-2)

def fibo2(n):
    fibos = [1,1]
    if n < 3:
        return fibos[n-1]
    else:
        for i in range(2,n):
            fibos.append(fibos[i-1]+fibos[i-2])
    return fibos[n-1]

def fibo3(n):
    a,b,c = 1,1,2
    for i in range(n - 3):
        a,b = b,c
        c = a+b
        #print(a,b,c)
    return c

now = time.time()

n = 3
while fibo3(n) < 10**999:
    n += 1
then = time.time()
elapsed = then - now
print(n,elapsed)

'''the recursive one took way too long!
now = time.time() 
f = fibo(100)
then = time.time()
elapsed = then - now
print(f,elapsed)'''

#fibo2(100) was instantaneous
#fibo2(1000) took 0.0005 seconds
'''now = time.time()
f = fibo2(1000)
then = time.time()
elapsed = then - now
print(f,elapsed)'''

'''now = time.time()
f = fibo3(1000)
then = time.time()
elapsed = then - now
print(f,elapsed)'''

