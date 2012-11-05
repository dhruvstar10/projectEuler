# a solution to problem 26 of project euler
# http://projecteuler.net/problem=26
# Find d<1000, for which 1/d contains the longest recurring cycle
# in its decimal part
# this solution is based on the following facts/logic
# * A mod B can have at most B different values for all A, from 0 to B-1
# * When long dividing A/B, if we get a remainder we have seen before, then the series of remainders will start repeating
# * Hence for 1/B, we only need to calculate at most till B decimal places.
# * The cycle for 1/B can be at most B long.
# * Hence, if we find a longest cycle that is X long, we don't need to check any 1/Y, for Y<X.

from util import *

# initialize
longestCycleLength = 0  # length of the longest cycle found yet
longestCycleDivisor = 0 # the corresponding divisor
d = 999    # current divisor, starting with max

# looping through different values of d
while (d > longestCycleLength):
	# find the length of the current divisor's cycle
	currentLength = getDecimalCycleLength(1,d)
	# if it is longer than the current max, update current max
	if currentLength > longestCycleLength:
		longestCycleLength = currentLength
		longestCycleDivisor = d
	# decrement d to progress through loop
	d -= 1

print "longest cycle is this long", longestCycleLength, "for this divisor", longestCycleDivisor
