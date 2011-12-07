# Problem 3 of project Euler
# Find largest prime factor of a given number

import math

input = 600851475143

current_dividend = input
end_point = math.sqrt(current_dividend)
largest_prime_factor = 1
current_divisor = 2
while current_divisor <= end_point:
	if current_dividend % current_divisor == 0:
		if current_divisor > largest_prime_factor:
			largest_prime_factor = current_divisor
		while current_dividend % current_divisor == 0:
			current_dividend /= current_divisor
		end_point = math.sqrt(current_dividend)
	else:
		current_divisor += 1

if largest_prime_factor == 1:
	print "largest prime factor is " + `input`
else:
	print "largest prime factor is " + `current_dividend`
