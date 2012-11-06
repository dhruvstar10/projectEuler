# a solution for problem 39 of project euler
# http://projecteuler.net/problem=39
# for a right triangle, with sides of length (a,b,c)
# p = a+b+c is the perimeter, and a^2 + b^2 = c^2
# find p <= 1000, for which the number of a,b,c solutions is maximized

from util import *

# initialize
maxSolutions = 0
maxP = 0
p = 1

while p <= 1000:
	currentNumSolutions = numPythagoreanTriplets(p)
	if currentNumSolutions > maxSolutions:
		maxSolutions = currentNumSolutions
		maxP = p
	p += 1

print "P =", maxP, "has maximum solutions =", maxSolutions
