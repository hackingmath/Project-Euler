'''Detrin's solution to Euler prob 23'''

import time
now = time.time()

Abund = [0 for i in range(28123)]
Abund_n = [1 for i in range(28123)]

for i in range(2, 28123):
	j = 1
	div_sum = 0
	while j**2 < i:
		if i % j == 0:
			div_sum += j + i / j
		j += 1
	if j**2 == i:
		div_sum += j
	div_sum -= i
	if div_sum > i:
		Abund[i] = 1

for i in range(28123):
	j = i
	while i + j < 28123 and j < 28123:
		if Abund[i] == 1 and Abund[j] == 1:
			Abund_n[i + j] = 0
		j += 1

			
sum_abund_n = 0
for i in range(28123):
	if Abund_n[i] == 1:
		sum_abund_n += i
print(sum_abund_n)
then = time.time()
elapsed = then - now
print(elapsed)

