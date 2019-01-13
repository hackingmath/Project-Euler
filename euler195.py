'''Problem 195
60-degree triangles'''

from math import sqrt, cos, degrees, pi

'''Go through Law of Cosines to find
all the triangles with integer sides,
find the inscribed circle's radius?'''

def convToRads(degrees):
    '''converts degrees to radians'''
    return degrees*pi/180

def lawofCos_c(a,b,C):
    '''Returns the side opposite the given angle in
    a triangle using the Law of Cosines
    Enter side, side, angle'''
    c = sqrt(a**2 + b**2 - 2*a*b*cos(convToRads(C)))
    return c

def heron(side1,side2,side3):
    '''Returns the area of a triangle given 3 side lengths'''
    semi = (side1 + side2 + side3)/2
    return sqrt(semi*(semi - side1)*(semi - side2)*(semi - side3))

def intTris():
    tris = 0
    triList = []
    for a in range(1,100000):
        for b in range(1,100000):
            c = lawofCos_c(a,b,60)
            #print(c)
            if a != b and abs(round(c)-c) <= 0.000001:
                c = round(c)
                triList.append([a,b,c])
    for tri in triList:
        a,b,c = triList[0],triList[1],triList[2]
        r = 2*heron(a,b,c)/(a+b+c)
        if r<=100:
            tris += 1
    print(tris)
