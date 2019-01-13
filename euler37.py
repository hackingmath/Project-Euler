'''Problem 37: Truncatable primes'''

#g = open('primelist.txt','r')
g = open('primes1.txt','r')
print("g:",type(g),"Opened Prime list. Now reading it...")
h = g.read()
print("h: ",type(h),"Now splitting it into a list...")
j = h.split()
k = [int(x) for x in j]
print("PrimeList is",len(j),"numbers long")
print (k[:10])
primes = [x for x in k if str(x)[0] in ['3','7'] and str(x)[-1] in ['3','7']]
print("The last 10 T-Primes are",primes[-10:])
'''for x in j:
    primes.append(int(x))'''

def isTPrime(n):
    strn = str(n)
    strn = strn.replace(' ','')
    '''if int(strn[0]) in [1,5,9] or int(strn[-1]) in [1,5,9]:
        return False'''
    #print(strn,type(strn))
    for i in range(len(strn)):
        if strn[:i] != '' and strn[i:] != '':
            print(strn[:i])
            if int(strn[:i]) not in k:
                return False
            print(strn[i:])
            if int(strn[i:]) not in k:
                return False
    return True

'''tprimes = [p for p in primes if isTPrime(p)]
tprimesInts = [int(p) for p in tprimes]
print(tprimes,sum(tprimesInts))'''
        

'''Output:
g: <class '_io.TextIOWrapper'> Opened Prime list. Now reading it...
h:  <class 'str'> Now splitting it into a list...
PrimeList is 1000000 numbers long
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
The last 10 T-Primes are [7999727, 7999753, 7999757, 7999787, 7999793, 7999813, 7999847, 7999913, 7999963, 7999993]
[3, 7, 37, 73, 313, 317, 373, 797, 3137, 3797, 739397] 748251
'''

