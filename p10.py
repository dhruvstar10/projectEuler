# a solution to problem 10 of project euler
# find the sum of all primes below 2 million

from util import *

sum = 2     				# starting with 2
current_num = 3 			# next num is 3
while current_num < 2000000:		# need to sum primes below 2 million
	if isPrime(current_num):	# check if number is prime
		sum += current_num	# add this prime to the sum
	current_num += 2		# evens are not prime

print sum				# output
