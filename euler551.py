''' Project Euler problem 551
Sum of Digits sequence
4/22/16'''

def sumdigs(n):
    '''returns the sum of the digits of n'''
    strn = str(n)
    sumdig = 0
    for digit in strn:
        sumdig += int(digit)
    return sumdig

def seq(n):
    a = [1]
    for i in range(n):
        print(sumdigs(a[-1]))
        a.append(sum(a[:-1])+sumdigs(a[-1]))
    return a[-1]

print(seq(7))
