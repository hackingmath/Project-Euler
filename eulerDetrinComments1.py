'''Detrin's solution to Euler prob 23
Comments by PF'''

import time
now = time.time()

Abund = [0 for i in range(28123)] #list for abundant numbers
Abund_n = [1 for i in range(28123)] #list for nums that are sums of abundants

#populate list of abundants
for i in range(2, 28123):
	j = 1 #divisor
	div_sum = 0 #sum of all divisors
	while j**2 < i:
		if i % j == 0: #if j is a divisor
                        #add j and i/j to the sum of divisors
			div_sum += j + i / j
		j += 1
	if j**2 == i: #if j is sqrt of i
		div_sum += j #add j to sum of divisors (once)
	div_sum -= i #the number isn't one of its own divisors
	if div_sum > i: #if the sum of divisors is more than the number
		Abund[i] = 1 #put a 1 in its place in the abundant list

#how to find the numbers that are sum of 2 abundants:
#go through abundant numbers and put a 0 with their sum in Abund_n
for i in range(28123):
	j = i
	while i + j < 28123 and j < 28123:
		if Abund[i] == 1 and Abund[j] == 1:
			Abund_n[i + j] = 0
		j += 1
			
sum_abund_n = 0
#go through list of nums that are sum of abundants
for i in range(28123):
	if Abund_n[i] == 1:
		sum_abund_n += i
print(sum_abund_n)
then = time.time()
elapsed = then - now
print(elapsed)

