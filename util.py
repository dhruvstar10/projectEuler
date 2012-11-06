# function to find factorial of number
def fact(n):
	if n <= 0:
		return 1
	elif n == 1:
		return 1
	else:
		return n*fact(n-1)


# function to check if number is palindrome
def isNumPalindrome(x):
	x_str = str(x)
	x_len = len(x_str)
	for i in range (0,x_len/2):
		if x_str[i] != x_str[x_len-(1+i)]:
			return 0
	return 1


# function to check if a number is prime
# currently handles x >= 2
def isPrime(x):
	import math
	end_point = int(math.sqrt(x))
	for i in range (2, end_point+1):
		if x % i == 0:
			return 0
	return 1


# function to return the number of factors of a number
# including 1 and the number itself
def numFactors(x):
	if x == 1:	# special/edge case
		return 1

	import math
	num_factors = 0		# initializing
	end_point = int(math.sqrt(x))	# need to check only till sq root
	for i in range (1, end_point+1):
		if x % i == 0:
			num_factors += 2	# +1 for i, +1 for x/i
	
	# if x is a perfect square, subtract 1 as its square root was added twice
	if end_point * end_point == x:
		num_factors -= 1
	
	return num_factors	# return the number of factors
		

# function to return the xth triangle number
# the xth triangle number is the sum of the first x natural numbers
def triangle(x):
	sum = 0
	for i in range (1, x+1):
		sum += i
	return sum

# function to return an array of unique divisors/factors of a natural numbers (integers > 0)
# the divisors include the 1 and the number itself
# the divisors in the array are not in any particular order
# x must be an integer greater than 0
def getDivisors(x):
	# initialize return array of divisors
	divisorArray = []

	import math
	end_point = int(math.sqrt(x))	# need to check only till floor of sq root
	for i in range (1, end_point+1): # check from 1 to including end point
		if x % i == 0:
			divisorArray.append(i)		# i is a divisor, append it
			divisorArray.append(x/i)	# if i is a divisor, so is x/i
	
	# if x is a perfect square, the square was added last and twice. Remove the copy.
	if end_point * end_point == x:
		divisorArray.pop()
	
	return divisorArray

# function to calculate sum of proper divisors of x, which are less than x
# this function does not handle x = 0. This is to improve efficiency and reduce this
# extra check for all x.
def getDivisorSum(x):
	return sum(getDivisors(x)) - x	# because divisors of x includes x

# function to get the length of the recurring cycle in the decimal part of a/b
# should return 0 if there is no recurring cycle
# So, for example, 1/7 = 0.(142857)(142857)..., and the length of the cycle is 6
# This function simulates long division
def getDecimalCycleLength(a,b):
	# First get rid of the integer part
	a = a % b

	# a list of remainders seen till now
	remainders = []
	while(a):	# terminate loop if decimal terminates
		# a is the current remainder, check to see if it has been seen before
		if a in remainders:
			# yes a has been seen before, so we will be entering a decimal cycle now if we continue
			return len(remainders) - remainders.index(a)
		else:
			# a is seen for the first time, so add it to list of already seen remainders
			remainders.append(a)
		# a is the current remainder that needs to be divided by b
		a *= 10
		if a > b:	# can divide only if a > b
			a = a % b	# get next remainder
	# loop termination implies that a was 0
	return 0

# function to get the number of integral pythogorean triples given the perimeter p
# find number of integral (a,b,c) solving a+b+c = p and a^2 + b^2 = c^2 
def numPythagoreanTriplets(p):
	# start by assuming a value of a, and then getting b and c and see if they make sense
	# then loop through values of a

	# initialize
	a = 1
	numSolutions = 0
	pythagoreanNumbers = [] # save values already calculated to avoid duplicate answers
	
	while a < p/2:
		# now need to solve 2 equations in 2 variables
		p_minus_a = float(p - a)
		a_square = a*a
		b = (p_minus_a - (a_square/p_minus_a))/2
		c = (p_minus_a + (a_square/p_minus_a))/2

		# now verify that the values we have form a pythagorean triplet
		b = int(b)
		c = int(c)

		if ((a*a) + (b*b) == (c*c)) and not(a in pythagoreanNumbers):
			# add a, b and c to already seen solutions
			pythagoreanNumbers.append(a)
			pythagoreanNumbers.append(b)
			pythagoreanNumbers.append(c)

			# got a new solution
			numSolutions += 1
		
		a += 1	# progress loop
	
	return numSolutions

