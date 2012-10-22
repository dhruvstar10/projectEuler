# a program to solve problem 21 of project euler
# http://projecteuler.net/problem=21
# find the sum of all amicable numbers under 10000
# d(n) is the sum of proper divisors of n excluding n.
# if d(a) = b, and d(b) = a, and a!=b then a and b are an amicable pair, and
# each of them is an amicable number

# import some utils
from util import *

# define a dictionary to store d(x) for all x between 1 and 9999
# set divisor sum of 0 to be 0, to avoid calculating divisorSum for 0, which the function can't do
divisorSum = {0:0}

# Calculate d(x)
for i in range (1, 10000):
	divisorSum[i] = getDivisorSum(i)

# initialize sum of amicable numbers
amicableSum = 0
for i in range (1, 10000):
	potentialPartner = divisorSum[i]	# d(i) = b, say
	if potentialPartner != i:		# ensure d(i) != i
		potentialPartnerDivisorSum = 0		# initialize potential value for d(b)
		if potentialPartner in divisorSum:	# then we have calculated d(b) already
			potentialPartnerDivisorSum = divisorSum[potentialPartner]	# d(b)
		else:					# need to calculate d(b)
			potentialPartnerDivisorSum = getDivisorSum(potentialPartner)	# d(b)
			# store this sum to reuse information
			divisorSum[potentialPartner] = potentialPartnerDivisorSum
		
		# now that we have the d(b), if that is equal to i, then i is an amicable number
		if i == potentialPartnerDivisorSum:
			# add it to the sum
			amicableSum += i


print "The sum of all amicable numbers less than 10000 is", amicableSum
