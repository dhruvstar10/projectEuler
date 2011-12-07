# solution to problem 4 of project euler
# find largest palindrome that is a product of two 3-digit numbers

from util import *

n1 = 999	# current number 1
l = 100		# lower bound for the 2 numbers

# solution relies on filling out a 999x999 table with products and
# checking which ones are palindromes
# We start with n1*n2 and loop by reducing n2 first.  As soon as we find
# a palindrome, we are done with that n2, as a lower n2 will give us a smaller product
# This effectively creates a lower bound l for the 2 numbers.  
# Also, if we find that the product is lower than current max product, there is no
# point reducing n2 further and we can get another lower bound
# We start again with n1 = n1-1
# and n2 = n1 (we don't need to calculate upper half of table)

largest_p_product = 0		# largest palindrome product

while n1 >= l:
	n2 = n1  # current number 2
	while n2 >= l:
		product = n1 * n2
		if product <= largest_p_product:
			l = n2 + 1
		elif isNumPalindrome(product):
			largest_p_product = product
			l = n2 + 1
		else:
			n2 -= 1
	n1 -= 1

print largest_p_product
		
		
