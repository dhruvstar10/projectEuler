# a solution to problem 30 or project euler
# http://projecteuler.net/problem=30
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

# We need to find numbers that can be written as the sum of fifth powers of their digits
# The upper bound for that is 999999 because
# 9^5 + 9^5 + 9^5 + 9^5 + 9^5 + 9^5 = 354294
# For any number larger than 999999, the sum of the fifth powers of its digits will definitely be less
# than the value of the number.

# store the fifth powers of digits, so we can just reuse them
digitFifthPowers = map(lambda x: x**5, range(0,10))

# helper method to calculate sum of fifth powers of the digits of a number
def getSumOfDigitFifthPowers(x):
    # split the number into an array of its constituent digits
    digitArray = map(lambda x: int(x), list(str(x)))
    # fetch the fifth power of each digit
    fifthPowerOfDigitsArray = map(lambda x: digitFifthPowers[x], digitArray)
    return sum(fifthPowerOfDigitsArray)

# now calculate sum of eligible numbers
answerSum = 0
for i in range(2,999999):
    if i == getSumOfDigitFifthPowers(i):
        answerSum += i

print "Sum of numbers is", answerSum