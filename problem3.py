# /home/daniohlala/Desktop python

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""

__author__ = "Daniela Valdez"
__email__ = "dani.ohlala@gmail.com"

import math

#-------------------------------------------------------------------------------------------------#


def factoresprimos(n):
	
	factors = []

	while n % 2 == 0:
		factors.append(2)
		print(2)
		n = n / 2

	for i in range(3, int(math.sqrt(n))+1, 2):
		while n % i == 0:
			factors.append(i)
			print(i)
			n = n / i

	if n > 2:
		factors.append(n)
		print(n)

	return factors

k = 600851475143
factores = factoresprimos(k)
print(factores)
print(max(factores))
 