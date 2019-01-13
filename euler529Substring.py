'''Project Euler problem 529
'''

import time
    
def subStr(num):
    '''returns True if num is 10-string friendly'''
    numList = [int(x) for x in str(num)] #puts digits in list
    yesDigits = [] #list of 10-sub friendly digits
    for i in range(len(numList)):
        for j in range(i,len(numList)+1):
            #print(numList[i:j])
            if sum(numList[i:j]) == 10:
                yesDigits.extend(range(i,j))
        if i > 0:
            if i - 1 not in yesDigits:
                return False
    #check whether all digits are friendly
    for k in range(len(numList)):
        #print("k=",k)
        if k not in yesDigits:
            return False
    return True
    
#print(subStr(55464553))

def T(n):
    '''returns number of 10-substring friendly 
    numbers from 1 to 10**n inclusive'''
    yesnum = 0
    for i in range(1,10**n + 1):
        if subStr(i):
            yesnum += 1
    return yesnum

#now1 = time.time()
#print("T(2)=",T(2),"T(5)=",T(5))
#print("T(10**18)%1000000007=",T(10**18)%1000000007)
#print("T(9)=",T(9))
#now2 = time.time()
#print(now2 - now1)

'''T(0) = 0, in 0 seconds
T(1) = 0, in 0 
T(2) = 9, in 0.003 seconds
T(3) = 72 in 0.045 seconds
T(4) = 507 in 0.47 seconds
T(5) = 3492 in 5.6 seconds
T(6) = 23697 in 63.3 seconds
T(8)= 1057941
T(9)= 7012665'''

def f():
    digits = []
    sum1 = 0
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                for g in range(1,10):
                    for h in range(1,10):
                        if h+g+i + j + k == 10:
                            print(str(h)+str(g)+str(i)+str(j)+str(k))
                            sum1 += 1
    print (sum1)

f()
                
