'''Euler Problem 66
Diophantine Equation
'''

from math import sqrt

def dio(D):
    '''returns minimal solution to
    x**2 - D*y**2 = 1'''
    y = 1
    while True:
        x = sqrt(1+D*y**2)
        #print("D: ",D,"x: ",x,"y: ",y)
        if x == int(x):
            return x
        y+=1

def dio2():
    for y in range(1,100000000):
        D = (2178548422**2 - 1)/y**2
        if D <= 1000 and D == int(D): #if D is an integer
            print("D: ",D,"y: ",y)
    
#dio2()

def maxDio():
    maxX = 0
    squares = [i**2 for i in range(40)]
    ds = [x for x in range(1,1001) if x not in squares]
    for i in ds:
        x = dio(i)
        if x > maxX:
            maxX = x
            print("so far:",maxX,"D: ",i)
    print("maxX = ",maxX)

maxDio()

'''
The results: 
so far: 3.0 D:  2
so far: 9.0 D:  5
so far: 19.0 D:  10
so far: 649.0 D:  13
so far: 9801.0 D:  29
so far: 24335.0 D:  46
so far: 66249.0 D:  53
so far: 335159612.0 D:  61
so far: 372326272.0 D:  109
so far: 498062163.0 D:  151
so far: 640500731.0 D:  199
so far: 667137236.0 D:  271
so far: 770394803.0 D:  331
so far: 959700061.0 D:  461
so far: 1110550906.0 D:  517
so far: 1592796237.0 D:  617
so far: 2178548422.0 D:  778
maxX =  2178548422.0
This takes a good 15 minutes to crank through.
However, PE says D = 778 is not correct.
'''
