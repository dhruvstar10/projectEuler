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
