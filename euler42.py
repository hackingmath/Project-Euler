'''Project Euler Problem 42
Coded Triangle Numbers'''

import time
#from urllib.request import urlopen

now = time.time()

#generate list of triangular numbers
tris = [x*(x+1)/2 for x in range(1,101)]

#Generate indices of alphabet
ALPHA = "abcdefghijklmnopqrstuvwxyz".upper()
ALPHA = {c:i+1 for i,c in enumerate(ALPHA)} # make it into a dict

#open the text file with the number triangle and read it:
#f = urlopen('https://projecteuler.net/project/resources/p067_triangle.txt').read()
f = open('euler42.txt','r').read()

#make it into a list of strings
g = f.split('","')
g[0].replace('"',"") #take out beginning and ending "
g[-1].replace('"',"")

def wordValue(str):
    '''adds up the value of the letters of a number'''
    val = 0
    for letter in str:
        if letter == '"':
            continue
        val += ALPHA[letter]
    return val

tot = 0
        
for word in g:
    w = wordValue(word)
    if w in tris:
        print(word,w)
        tot += 1

print(tot)
        
then = time.time()
elapsed = then - now
print(elapsed)

# 162 Correct in 0.55 seconds
# My 50th PE problem!

