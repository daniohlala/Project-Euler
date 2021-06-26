# /home/daniohlala/Desktop/PE python

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

__author__ = "Daniela Valdez"
__email__ = "dani.ohlala@gmail.com"


import math

#-------------------------------------------------------------------------------------------------#



"""

for i in range(2, n+1):
    primes.append(i)

i = 2

while 
    while i <= (int(math.sqrt(n))+1):
        if i in primes:
            for j in range(i*2, n+1, i):
                if j in primes:
                    primes.remove(j)
        i = i + 1


print(primes)   """

primes = []
primes.append(2)
k = len(primes)

i = 3

while k < 10:
    for j in range(2, i+1):
        if i % j == 0:
            break
    if i == j:
        primes.append(i)
        k = k + 1
                        
    i = i + 1 

print(primes[5])