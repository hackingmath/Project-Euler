'''Problem 26 solution by Brian'''

import time

import itertools
def recur_len(n):
    # digits for unit fraction 1/n
    r = 10 # initial remainder (10/n)/10
    seen = {} # remainder -> first pos
    for i in itertools.count(0):
        if r == 0:
            return 0  # divides evenly.
        elif r in seen:
            return i-seen[r] # curpos - firstpos
        seen[r] = i
        r= 10*(r % n)

#len,i = max((recur_len(i),i) for i in range(2,1000))
#print (i)

'''solution by cycledbe'''

def period(d):
    n=10**len(str(d))
    count=0
    remainder=[]
    while (n%d not in remainder):
        remainder.append(n%d)
        n=(n%d)*10
        count+=1
    return count,d

now = time.time()
print('(max count, corresponding max d):', max(period(x) for x in range(2,1001)))
then = time.time()
elapsed = then - now
print(elapsed)
