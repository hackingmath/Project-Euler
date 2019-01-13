'''Pandigital Products'''

from itertools import permutations
import time

def farrell():
    '''My solution'''
    t1 = time.time()
    a = permutations('123456789')

    count  = 0
    prods = set()
    while True:
        try:
            b = next(a) #list of string objects
        
            c = ''
            #This will make the permutation a string
            for i in range(9):
                c += b[i] 

            #slice the string, convert to ints and check if multiplication works
            for i in range(1,3):
                for j in range(i,5):
                    x = int(c[j+1:])
                    if int(c[:i])*int(c[i:j+1])== x:
                        #print(int(c[:i]),int(c[i:j+1]),int(c[j+1:]))
                        #count += 1
                        prods.add(x)
        except StopIteration: #when permutations run out
            print(sum(prods)) #print the solution
            print(time.time() - t1) #and the elapsed time
            break
        #45228. Correct in 6.1 seconds!

def baffo():
    def pandig(i,j):
        n = i*j
        s = str(i) + str(j) + str(n)
        digSet = set(s)
        if '0' in s:
            return False
        if len(digSet)==9 and len(s)==9:
            return True
        else:
            return False
        

    prods=set()
    for i in range(0,100):
        for j in range(i,10000):
            if (pandig(i,j)):
                n=i*j
                prods.add(n)
                print(i,j,n)

    print(prods)
    print(sum(list(prods)))

def stefan():
    '''Stefan Pochmann'''
    p = set()
    for a in range(1, 100): #first factor 1 or 2 digits
        for b in range(1, 9999 // a): #second factor 1 to 4 digits
            #if the whole equation contains 1 - 9:
            if ''.join(sorted("%d%d%d" % (a, b, a*b))) == '123456789':
                p.add(a * b)
    print(sum(p))
