'''problem 92
Square digit chains'''
import time

def chain(n,list89):
    while n not in list89:
        if int(n) == 1:
            return False
        sum1 = 0
        n = str(n)
        for i in range(len(n)):
            sum1 += int(n[i])**2
        n = sum1
        if n == 89:
            return True
    return True

#print(chain(44))
list89 = []
now = time.time()
eighty_nines = 0
for i in range(1,10000000):
    if chain(i,list89):
        eighty_nines += 1
        list89.append(i)
print(eighty_nines)
now2 = time.time()
print(now2-now)


