# a solution to problem 20 of project euler
# find the sum of the digits of 100!

x = 1		# this will be 100 factorial without the trailing zeros
for i in range(2,101):
	x *= i
	if x%10 == 0:	# if divisible by 10, a 0 in the end, which doesn't contribute to the sum
		x /= 10

# now add the digits of x
sum = 0
while x>0:
	sum += (x % 10)		# add units digit
	x /= 10			# remove units digit and shift

print sum
