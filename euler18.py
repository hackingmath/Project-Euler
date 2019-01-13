'''Problem 18 Maximum path sum I'''

import time

t1 = time.time()

#copied and pasted this table:

cell = [[75],
        [95,64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20, 4, 82, 47, 65],
        [19, 1, 23, 75, 3, 34],
        [88, 2, 77, 73, 7, 63, 67],
        [99, 65, 4, 28, 6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

def maxPath():
    '''calculates the sum of each path through the
    triangle, keeps track of the running max.'''
    max1 = 5
    a=cell[0][0]
    for b in cell[1]:
        for c in cell[2][cell[1].index(b):cell[1].index(b)+2]:
            for d in cell[3][cell[2].index(c):cell[2].index(c)+2]:
                for e in cell[4][cell[3].index(d):cell[3].index(d)+2]:
                    for f in cell[5][cell[4].index(e):cell[4].index(e)+2]:
                        for g in cell[6][cell[5].index(f):cell[5].index(f)+2]:
                            for h in cell[7][cell[6].index(g):cell[6].index(g)+2]:
                                for i in cell[8][cell[7].index(h):cell[7].index(h)+2]:
                                    for j in cell[9][cell[8].index(i):cell[8].index(i)+2]:
                                        for k in cell[10][cell[9].index(j):cell[9].index(j)+2]:
                                            for l in cell[11][cell[10].index(k):cell[10].index(k)+2]:
                                                for m in cell[12][cell[11].index(l):cell[11].index(l)+2]:
                                                    for n in cell[13][cell[12].index(m):cell[12].index(m)+2]:
                                                        for o in cell[14][cell[13].index(n):cell[13].index(n)+2]:
                                                        
                                                            sum1 = a+b+c+d+e+f+g+h+i+j+k+l+m+n+o
                                                            if sum1 > max1:
                                                                z = (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o)
                                                                max1 = sum1
                                                                
    print(max1,z) #correct answer in 0.0357 seconds

def maxPath2():
    '''more efficient way to get the sum "manually"? Not finished'''
    sum1 = 0
    max1 = 0
    col = 0
    for row in range(15):
        for col in [col,col+1]:
            sum += cell[row][col]
    
    
def maxcell(r,c):
    '''Recursive function for finding the path through the
    triangle with the maximum value'''
    if r == 14: #if it's in the last row
        return cell[r][c] #return the value of that cell
    else: #otherwise return the cell + the max of the lower two cells
        return cell[r][c] + max(maxcell(r+1,c),maxcell(r+1,c+1))

#maxPath()
print(maxcell(0,0)) # is 1074 in 0.031 seconds
t2 = time.time()
print(t2 - t1)
