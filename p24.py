# the solution for problem 24 of project euler
# the 1 millionth lexicographical permutation using all digits 0-9
# 0123456789 is a valid permutation

from util import *

perm_left = 999999                       # permutations left to compute
num_digits = 9                           # number of digits currently being permuted
digits_available = [0,1,2,3,4,5,6,7,8,9] # digits available for permutations in ascending order
result_arr = []     # result array

while perm_left > 0:
	current_max_perm = fact(num_digits) # the maximum number of permutations possible if permuting all of current digits
        if current_max_perm > perm_left:
		next_digit = digits_available.pop(0)
		result_arr.append(next_digit)
	else:
		x = perm_left/current_max_perm
		next_digit = digits_available.pop(x)
		result_arr.append(next_digit)
		perm_left -= x*current_max_perm
	num_digits -= 1
	print "perm_left " + `perm_left`
	print "result_arr "
	print result_arr

print result_arr
print digits_available
		
