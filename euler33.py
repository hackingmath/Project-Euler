'''Project Euler Problem 33
Digit cancelling Fractions'''

def cancel(numerator,denominator):
    '''checks if there's any cancelling possible'''
    n = str(numerator)
    d = str(denominator)
    if numerator == denominator: return False
    if n[0] not in d and n[1] not in d:
        return False
    if n[0] == d[0] and n[0] != '0':
        if '0' in d: return False
        simp = int(n[1])/int(d[1])
        if simp == numerator/denominator:
            print(simp)
            return True
    elif n[0] == d[1] and n[0] != '0':
        if '0' in d: return False
        simp = int(n[1])/int(d[0])
        if simp == numerator/denominator:
            print(simp)
            return True
    elif n[1] == d[0] and n[1] != '0':
        if '0' in d: return False
        simp = int(n[0])/int(d[1])
        if simp == numerator/denominator:
            print(simp)
            return True
    elif n[1] == d[1] and n[1] != '0':
        if '0' in d: return False
        simp = int(n[0])/int(d[0])
        if simp == numerator/denominator:
            print(simp)
            return True
    else: return False

simps = []
for i in range(11,100):
    for j in range(i,100):
        if cancel(i,j):
            print(i,j)

