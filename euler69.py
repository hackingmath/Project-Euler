'''Problem 69 Totient maximum
Brute force first, and it took hours to go through
20,000 numbers, so how to do a million?
But I don't see a pattern'''

import time

t1 = time.time()

def relPrime(n):
    '''returns number of relatively prime'''
    phi = [x for x in range(1,n)]
    for i in range(1,n):
        #print("i:",i)
        if n % i == 0 and i in phi and i != 1:
            phi.remove(i)
            for j in range(i,n):
                #print("j:",j)
                if j in phi and j % i == 0:
                    phi.remove(j)
    #print(phi)
    return phi

def totient(n):
    '''returns n/phi(n)'''
    return n/len(relPrime(n))

for i in range(10,1001,10):
    print(i,len(relPrime(i)))
    
'''maxtot = 1
for i in range(10010,100001,10):
    tot = totient(i)
    if tot > maxtot:
        print(i,tot)
        maxtot = tot'''
        
    #tots[i] = totient(i)

#print(max(tots, key = tots.get))

#print(maxtot)
t2 = time.time()
#print(t2 - t1)
