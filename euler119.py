'''Project Euler Problem 119
Digit Power Sum'''

def isIt(n):
    '''checks n's sum to see if n
    is the sum raised to a power.'''
    nstr = str(n)   #change number to a string
    sum1 = 0        #running sum of digits
    for i in range(len(nstr)): #go through whole string
        sum1 += int(nstr[i])   #add each digit
        if sum1 == 1:       #if the sum is 1 --> infinite loop
            return False
    power = 1 #check all powers of the sum until they're bigger than n
    while sum1**power < n: #if sum to power is less than n
        power += 1         #try the next higher power
    if sum1**power == n:   #this is the only True state
        return True
    if sum1**power > n:    #if the sum to the power is greater than n
        return False       #it's not "it"
    
num = 10
anums = 0

while anums < 30:
    if isIt(num):
        print(num)
        anums += 1
        if anums == 30:
            print(num)
            break
    num += 1
