# solution to problem 12 of project euler
# find the first triangle number to have over 500 divisors
# the nth triangle number is the sum of the first n natural numbers

from util import *

n = 1	# current index of the triangle number
t = 1	# current triangle number

while numFactors(t) <= 500:
	n += 1
	t += n

print "triangle number with over 500 divisors " + `t`
print "index of that triangle number " + `n`
print "Number of factors " + `numFactors(t)`
