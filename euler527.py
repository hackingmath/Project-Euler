'''Euler problem 527
https://projecteuler.net/problem=527'''

from random import randint

def binSearch(n):
    '''number of guesses needed to find a
    number in range n'''
    t = randint(1,n)
    lower = 1
    upper = n
    guesses = 0
    while True:
        #print("t=",t)
        #print("lower = ",lower)
        #print("upper = ",upper)
        guesses += 1
        guess = int((lower + upper)/2)
        #print("guess=",guess)
        if guess == t:
            return guesses
        elif guess < t:
            lower = guess+1
        else:
            upper = guess-1

def average(listA):
    return sum(listA)/len(listA)

def randSearch(n):
    '''number of guesses needed to find a
    number in range n'''
    t = randint(1,n)
    lower = 1
    upper = n
    guesses = 0
    while True:
        #print("t=",t)
        #print("lower = ",lower)
        #print("upper = ",upper)
        guesses += 1
        guess = randint(lower,upper)
        #print("guess=",guess)
        if guess == t:
            return guesses
        elif guess < t:
            lower = guess+1
        else:
            upper = guess-1
            
Bsearches = [] #binary search
Rsearches = [] #random binary search
for i in range(10000):
    Bsearches.append(binSearch(7))
    Rsearches.append(randSearch(7))
print(average(Rsearches)-average(Bsearches))

        
        
