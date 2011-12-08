# a solution to problem 7 of project euler
# find the 10001 st prime

from util import *

n = 5	# starting counting from the 5th prime onwards
p = 11  # the 5th prime is 11

while n < 10001:
	p += 2
	if isPrime(p):
		n += 1

print "10001st prime is " + `p`
