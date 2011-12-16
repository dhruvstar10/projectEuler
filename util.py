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
