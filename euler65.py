'''Project Euler problem 65
Convergents of e
Still doesn't work'''
from fractions import Fraction

def coeffs(n):
    '''returns the list of coefficients
    of the continued fraction for e'''
    e_list = []
    for i in range(n):
        e_list += [1,2*i,1]
    return e_list

#get a list of coefficients
c_list = coeffs(5//3 + 1)

e_sum = 1 #running sum   

def eFrac(n):
    global e_sum
    '''calculate the continued fraction for e'''
    if n == 0:
        return e_sum
    else:
        e_sum /= (c_list[n]+Fraction(1,eFrac(n-1)))
    #return e_sum

print(eFrac(5))
