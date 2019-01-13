'''problem 26: Reciprocal cycles'''
import time

def cycle(denominator):
    '''returns the recurring cycle of the
    decimal 1/d.'''
    cycle = [] #list to store digits of cycle
    #digit,remainder = divmod(10, denominator)
    #cycle.append(digit)
    remainder = 1
    while True:
        #this divides and give the quotient and remainder
        digit,new_remainder = divmod(10*remainder,denominator)
        #store digit and remainder info to check for repeat
        x = [digit,new_remainder]
        #print("x =",x)
        #print("cycle =",cycle)
        if x in cycle: #if that digit/remainder pair are already in cycle
            place = cycle.index(x) #find out where they are in the decimal
            #soln = [z[0] for z in cycle]
            ans = len(cycle) - place #subtract to find out how long the cycle was
            #print("soln=",soln,len(cycle) - place)
            return ans
        cycle.append(x) #otherwise put x in the cycle
        remainder = new_remainder #increment the remainder

now = time.time()
#create variable for maximum cycle length
max_cycle = 0
max_num = 0 #variable for maximum number

#go through all the numbers from 3 to 100
for i in range(3,1001):
    c = cycle(i) #check the cycle length
    if c > max_cycle: #if it's the max so far
        max_cycle = c #set max to that
        max_num = i
print(max_num, max_cycle) #print the number with the max

then = time.time()
elapsed = then - now
print(elapsed)
