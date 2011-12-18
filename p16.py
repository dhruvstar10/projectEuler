# a solution to problem 16 of project euler
# find the sum of the digits of 2^1000

x = 2**1000	# let the computer calculate
sum = 0		# initialize sum
while x > 0:
	sum += (x%10)	# add units digit
	x /= 10		# shift digits to the right

print sum
