'''Problem 22: Names scores'''

import time

t1 = time.time()

#first get "alphabetical value" of each letter
ALPHA = 'abcdefghijklmnopqrstuvwxyz'.upper()
ALPHA = {c:i+1 for i,c in enumerate(ALPHA)}

def alphaValue(name):
    '''adds up alpha values for letters'''
    sum1= 0
    for letter in name:
        sum1 += ALPHA[letter]
    return sum1

        

f = open('names.txt','r') #open the names file
text = f.read()         #read it into text form
names = list(eval(text)) #turn into a list
#print(names[:10])
names.sort()            #sort the list
#print(names[:10])


def nameValue():
    sum2 = 0
    for name in names:
        sum2 += alphaValue(name)*(names.index(name)+1)
    print(sum2)
    
nameValue()
#print(alphaValue('COLIN'), names.index('COLIN'))

f.close()

t2 = time.time()
print(t2 - t1)

'''Correct answer: 871198282
0.3169882297515869 seconds'''
