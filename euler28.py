'''Euler project problem 28
Number spiral diagonals

I have to make this kind of grid:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

and come up with the sum of all the
values on the diagonals.'''

def grid(n):
    '''n has to be an odd number'''
    gridn = [[1]]
    for j in range(3,n+2,2): #cycle this many times(3,5...)
        for i in range(1,j-1):        #add this many middle rows
            gridn[i-1].append((j-2)**2 + i) #add to the end of the middle rows
        bottom_row = [] #empty list for bottom row
        for k in range(j): 
            bottom_row.append((j-2)**2 + j-1+k) #add values to bottom row
        bottom_row.reverse()                #reverse them
        gridn.append(bottom_row)            #add them to grid
        gridn.insert(0,[j*(j-1)+k for k in range(1,j+1)]) #top row
        for i in range(j-2):
            gridn[j-2-i].insert(0,j*(j-2)+3 + i)    #first columns

    return gridn

g = grid(1001)
s1 = sum([g[n][n] for n in range(1001)])
s2 = sum([g[n][1000-n] for n in range(1001)])
s3 = s1 + s2 - 1
print(s3)

#simple solution by Niten:
'''s=0
for i in range(1001,1,-2):
    t = i**2
    for j in range(4):
        s += t - j * (i-1)
s+=1

print(s)'''

