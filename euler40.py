"""Project Euler prob. 40
Champernowne's constant"""
import time

t1 = time.time()

#create a list of all the numbers from 1 to a million
digits = [x for x in range(1000000)]

#convert the list to string
s = ''.join(str(e) for e in digits)

print(s[:20])
#convert the target terms to ints and multiply them
print (int(s[1])* int(s[10])* int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000]))

t2 = time.time()

print(t2 - t1)
