# a solution to problem 14 of project euler
# for the sequence
# n -> n/2 if n is even
# n -> 3n + 1 if n is odd
# which starting number less than 1 million
# results in the longest chain
# numbers are allowed to go over 1 million once the chain starts

# we'll use a dynamic programming approach to reduce recalculculations
# for example, the chain starting at 13 contains 10.  If we store the
# chain length starting with 10, we can stop calculating for 13 once we
# reach 10

# NOTE: might cause large function call stack due to recursice nature
# might be able to improve upon that if we make it tail recursive
# using a continuation passing style.  Don't know enough about python
# to know whether that would be optimized or not

# using numpy module to easily create empty array
from numpy import *

# array of size 10 million and 1
# value at index i represents chain length
# starting with number i
chain_lengths = zeros(10000001, int)
chain_lengths[1] = 1	# initializing index 1

# function to return chain length if starting with num
# also sets chain_lengths[num] if not stored and within array bounds
def calc_chain_length(num):
	if num == 1:		# termination condition
		return 1

	elif num <= 10000000:	# the max index we can store is 10 mil
		if chain_lengths[num] == 0:	# this value hasn't been calculated
			if num % 2 == 0:	# if num is even
				chain_lengths[num] = 1 + calc_chain_length(num/2)
			else:			# num is odd
				chain_lengths[num] = 1 + calc_chain_length(3*num+1)
		return chain_lengths[num]

	else:		# num is greater than 10 mil, can't save it, just return
		if num % 2 == 0:	# if num is even
			return 1 + calc_chain_length(num/2)
		else:			# num is odd
			return 1 + calc_chain_length(3*num+1)
		

# now calculate for all numbers
for i in range(2, 1000000):
	calc_chain_length(i)

# now search the array for the index with the max value
longest_chain_index = 0
longest_chain_length = 0
for i in range(1, 1000000):
	if chain_lengths[i] > longest_chain_length:
		longest_chain_length = chain_lengths[i]
		longest_chain_index = i

print longest_chain_length
print longest_chain_index
