# /home/daniohlala/Desktop/PE python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

__author__ = "Daniela Valdez"
__email__ = "dani.ohlala@gmail.com"


import math

#-------------------------------------------------------------------------------------------------#

n = 200000
primes = []
for i in range(2, n+1):
    primes.append(i)

i = 2


while i <= (int(math.sqrt(n))+1):
    if i in primes:
        for j in range(i*2, n+1, i):
            if j in primes:
                primes.remove(j)
    i = i + 1

suma = 0

for j in primes:
	suma = suma + j

print(suma)
