'''Largest Palindromic Product'''

def is_palin(num):
    strnum = str(num)
    return strnum[::-1] == strnum

def three_digit_products():
    '''Multiplies all 3-digit numbers together?'''
    output = []
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            prod = i*j
            if is_palin(prod):
                output.append(prod)
    return max(output)

print(three_digit_products())
