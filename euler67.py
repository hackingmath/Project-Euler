'''Project Euler Problem 67
Maximum path sum II
the non-recursive method'''

import time
from urllib.request import urlopen

now = time.time()

#open the text file with the number triangle and read it:
f = urlopen('https://projecteuler.net/project/resources/p067_triangle.txt').read()

#make it into a list of strings
g = f.split()

#make another list and convert the strings to ints
h = [int(x) for x in g]

#Make it into an array:
tri = [] #new list 
count = 0 #variable to count the entries
for i in range(100): #for each row in tri
    tri.append([]) #make an empty list to contain the row
    for j in range(i+1): #1 more time than i
        tri[i].append(h[count]) #put that many items of h in that row
        count+=1    #go to the next item in h

    
for r in range(98,-1,-1): #start at the second row from the bottom
    for c in range(r+1):  #columns go from 0 to r
        #to each cell in the row, add the max of the two cells below it
        tri[r][c] += max(tri[r+1][c],tri[r+1][c+1])

print(tri[0][0]) #what's the top one?

then = time.time()
elapsed = then - now
print(elapsed)

# 7273 Correct!
# read from local txt file in 0.04 seconds.
# read from url in 1.754 seconds

