'''Problem 62 cubic permutations'''

import time
from itertools import permutations

t1 = time.time()

cubes = [x**3 for x in range(1001,10000)]


def make_list(cube):
    cubestring = str(cube)
    #print(cubestring)
    cubelist = [int(x) for x in cubestring]
    cubelist.sort()
    return cubelist#.sort()

cube_lists = {x:make_list(x) for x in cubes}

#print(cube_lists)

#print(make_list(1234**3))

for cube in cube_lists.values():
    sames = []
    for cube2 in cube_lists.values():
        if cube == cube2:
            sames.append(cube)
            sames.append(cube2)
    if len(sames) == 5:
        print(sames)

def fact(n):
    if n<=1: return 1
    return n*fact(n-1)

def permut(n):
    tot = 0
    '''returns a list of all the permutations of n'''
    plist = set()
    nstr = str(n)
    p = permutations(nstr)
    for i in range(fact(len(nstr))):
        tempstr = ''
        t = next(p)
        #print("next p:",t)
        for digit in t:
            tempstr += digit
        
        #print(tempstr,"plist:",plist)
        if int(tempstr) in cubes:
            print("Found cube:",tempstr,"plist:",plist)
            plist.add(int(tempstr))
            tot += 1
        if len(plist) == 5:
            return plist
    return
        #plist.append(int(tempstr))
    '''for n in plist:
        if n in cubes:
            print("Found cube:",n)
            tot += 1
    return tot'''

#permut(1234**3)
'''for c in cubes[:5]:
    if permut(c) == 5:
        print("solution:",c)
        break'''

t2 = time.time()

print(t2-t1)

#
