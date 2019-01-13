import time

'''This was suggested by Brian on PE forum. It returned the answer in less
than a second.'''

t1 = time.time()
Limit=1000000000     # Search under 1 million for now
factors=[0]*Limit # number of prime factors.
count=0
for i in range(2,Limit): #from 2 to a million
    #print(factors)
    if factors[i]==0:   #if the entry is 0
        # i is prime
        count =0 
        val =i
        while val < Limit:
            factors[val] += 1 #increase the factors of val
            val+=i          #increase all the factors of i
    elif factors[i] == 5:
        count +=1
        if count == 5:
            print(i-4) # First number
            break
    else:
        count = 0

t2 = time.time()
print(t2 - t1)
