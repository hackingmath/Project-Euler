'''problem 92
Square digit chains'''
import time

def chain(n):
    while True:
        if int(n) == 1:
            return False
        sum1 = 0
        n = str(n)
        for i in range(len(n)):
            sum1 += int(n[i])**2
        n = sum1
        if n == 89:
            return True

#print(chain(44))
now = time.time()
eighty_nines = 0
for i in range(1,10000000):
    if chain(i):
        eighty_nines += 1
print(eighty_nines)
now2 = time.time()
print(now2-now)
    
#brute force 133.13 s
#moved if statement --> 133.29 s


