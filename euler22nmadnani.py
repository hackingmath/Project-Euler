#by nmadnani on PE forum

import string
from time import *

start = clock()
valuehash = dict(zip([x for x in string.letters[26:]],range(1,27)))
names = [x[1:-1] for x in string.split(open('names.txt','r').read()[:-1],',')]
names.sort()
namescores = [sum([valuehash[x] for x in names[i]])*(i+1) for i in range(len(names))]
print ("Sum = %d" % sum(namescores))
print ("Time taken = %.2f" % (clock()-start))

#I get an AttributeError: module 'string' has no attribute 'letters'
