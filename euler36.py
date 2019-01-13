'''Project Euler Problem 36
Double base palindromes'''

def binary(number):
    '''Converts decimal number to binary'''
    exponent = 0    #We're dealing with exponents of 2
    binary_number = 0           #The binary form of the number
    while number >= 2**exponent:#Finds the lowest power of 2
        exponent += 1           #the number is less than
    exponent -= 1
    for i in range(exponent + 1):
        if number - 2**exponent > -1: #if number contains power of 2
            binary_number += 10**exponent #add that power of 10
            number -= 2**exponent #Take away that power of 2 from number
        exponent -= 1           #Next lower exponent
    return binary_number

def palindrome(num):
    '''Returns true if number is same
    backwards and forwards'''
    return num == int(str(num)[::-1])

palis = 0
for x in range(1000001):
    if palindrome(x) and palindrome(binary(x)):
        print(x, binary(x))
        palis += x

print(palis)
