'''Problem 24 solution by gcapell'''

from math import factorial
import time

def nthPerm(s, n):
	if len(s)<2:
		return s
	quot, n = divmod(n, factorial(len(s)-1))
	return s[quot] + nthPerm(s[:quot] + s[quot+1:], n)

now = time.time()
print (nthPerm('0123456789', 1000000 - 1))
then = time.time()
print(then - now)
