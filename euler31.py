'''Euler Problem 31 Coin Sums
Brute force. Print out every combination'''

import time
t1 = time.time()

def coinSum():
    count = 0
    for p in range(0,201):#pence
        for t in range(0,101):#tuppence
            for f in range(0,41): #5p
                for tenp in range(0,21):
                    for p20 in range(0,11):
                        for p50 in range(0,5):
                            for pound in range(0,3):
                                if p + 2*t + 5*f + 10*tenp +\
                                   20*p20+50*p50+100*pound == 200:
                                    #print(p,t,f,tenp,p20,p50,pound,"count",count)
                                    count += 1
    print(count+1) #add one because didn't include 2pound coin.

coinSum()
print(time.time() - t1)
#answer 73682 correct in 18.85 minutes :-|
