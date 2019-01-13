'''Project Euler Problem 14
The Collatz Sequence:
if n is even: n --> n/2
if n is odd: n --> 3n + 1
How many steps does it take to get to 1?
Recursive formula'''

import time

t1 = time.time()

cols = {0:0,1:0}

def collatz(n):
    '''Returns the number of steps it
    takes to get to 1'''
    chain = 0 #number of steps
    while True: # "do this forever"
        #print(n) #uncomment to check steps
        if n == 1:
            return chain
        #if n has already been checked:
        elif n in cols:
            return chain + cols[n]
        elif n % 2 == 0: #if n is even
            chain = 1 + collatz(n/2)
            cols[n] = chain
            return chain
        else: #n is odd
            chain = 1 + collatz(3*n + 1)
            cols[n] = chain
            return chain
        #chain += 1

def longestSeq():
    '''Records the length of the sequence'''
    n = 2 #start at 2
    while n<1000000: #check every number less than a million
        collatz(n) #add to cols dict
        n += 1  # check the next number
    #find the number with the longest chain
    m = max(cols,key=cols.get)  
    print(m,"steps:",cols[m]) #print it out

longestSeq()
    
t2 = time.time()
print("elapsed:",t2-t1)
