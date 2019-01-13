'''Self powers
find last 10 digits of series
1**1 + 2**2 + 3**3 + ... + 1000**1000'''

def series(n):
    sum1 = 0
    for i in range(1,n+1):
        sum1+=i**i

    return sum1

print(series(10**3))

#answer: 9110846700
        
