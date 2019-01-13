'''Problem 19 Counting Sundays'''

#1/1/1900 was a Monday

def sundays():
    firsts = [[1]] #monday
    monthdays = [31,28,31,30,31,30,31,31,30,31,30,31]
    monthdays2= [31,29,31,30,31,30,31,31,30,31,30,31]
    for k in range(11):
        firsts[0].append((firsts[0][k] + monthdays[k])%7) #fill in the months
    for i in range(1,101): #do this from 1 to 100 years
        firsts.append([])
        for j in range(12): #for every month
            if j in [0,1]: #Jan and Feb are staggered
                if (i-1) % 4 == 0 and i != 1: #leap year
                    firsts[i].append((firsts[i-1][j]+366)%7) #add the number of days in a year
                else: #no leap year
                    firsts[i].append((firsts[i-1][j]+365)%7)
            else: #March - December
                if i % 4 == 0: #leap year
                    firsts[i].append((firsts[i-1][j]+366)%7) #add the number of days in a year
                else: #no leap year
                    firsts[i].append((firsts[i-1][j]+365)%7)

    sumOfSundays = 0
    for year in firsts:
        sumOfSundays += year.count(0)

    print(sumOfSundays - 2)
#There were 173 Sundays, but I've included 1900, which had 2 Sundays. S0 171 is correct.

'''Here's an easier way using datetime:'''

import datetime
count = 0
for y in range(1901,2001):
    for m in range(1,13):
        if datetime.datetime(y,m,1).weekday() == 6:
            count += 1
print (count)
