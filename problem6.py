# /home/daniohlala/Desktop/PE python

"""
The sum of the squares of the first ten natural numbers is, 

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

__author__ = "Daniela Valdez"
__email__ = "dani.ohlala@gmail.com"

#-------------------------------------------------------------------------------------------------#

sum_of_squares = 0
square_of_sum = 0
suma = 0
dif = 0

for i in range(1,100+1):
	sum_of_squares = sum_of_squares + i**2

for i in range(1,100+1):
	suma = suma + i
square_of_sum = suma**2

print(sum_of_squares)
print(square_of_sum)

dif = square_of_sum - sum_of_squares
print(dif)	


