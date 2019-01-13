'''Problem 67 Maximum path sum II'''

import time
from urllib.request import urlopen

t1 = time.time()

txt = urlopen('https://projecteuler.net/project/resources/p067_triangle.txt').read()
b = txt.split()
cell = []
n = 0 #for counting elements of b
for i in range(100): #for each row
    cell.append([]) #empty list
    for j in range(i+1): #put this many elements in row
        cell[i].append(int(b[n])) #put the next elements of b
        n += 1 #keep going through b list

def maxcell(r,c):
    '''returns the sum of the cell and the max of the
    cells lower down'''
    if r == 99:
        return cell[r][c]
    else: #recursion!
        return cell[r][c] + max(maxcell(r+1,c),maxcell(r+1,c+1))

print(maxcell(0,0)) # is ??? No output after a few hours.
t2 = time.time()
print(t2 - t1)
