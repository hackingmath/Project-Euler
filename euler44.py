"""Project Euler prob. 44
Pentagon Numbers
Feb 20, 2016"""
import time

t1 = time.time()

#create a list of all the Pentagonal numbers from 1 to a million
pnums = [x*(3*x-1)/2 for x in range(1,10000)]

#print(pnums[:20])

pmin = 100

for i in range(len(pnums)):
    for j in range(i+1, len(pnums) - i):
        sum1 = pnums[i] + pnums[j]
        diff = abs(pnums[i] - pnums[j])
        if sum1 in pnums and diff in pnums:
            print(pnums[i],pnums[j])
            if diff < pmin:
                pmin = diff
                print(pnums[i],pnums[j])

#the two pentagonal numbers are 1560090 and 7042750! 
t2 = time.time()

print(t2 - t1)
