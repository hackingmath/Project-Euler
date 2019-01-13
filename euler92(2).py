'''problem 92
Square digit chains
I was trying to check a "Go To 89" list
to get out of trying numbers, but that's
getting confusing.'''
import time

#print(chain(44))
now = time.time()
go_to_89 = [] #list for numbers that go to 89
eighty_nines = 0
for n in range(1,10000000):
    while True:
        print(n,go_to_89)
        if n in go_to_89:
            eighty_nines += 1
            break
        elif n == 89:
            eighty_nines += 1
            go_to_89.append(n)
            break
        elif n == 1:
            break
        else:
            sum1 = 0
            strn = str(n)
            for i in range(len(strn)):
                sum1 += int(strn[i])**2
            n = sum1
                
print(eighty_nines)
now2 = time.time()
print(now2-now)
    
#never printed!


