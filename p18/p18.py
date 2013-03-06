# a program to solve problem 18 of project euler
# http://projecteuler.net/problem=18
# read a pyramid of numbers and find the maximal sum on a path from top to bottom
# Approach: Dynamic programming - Find the maximal sum from a root node, based on the
# maximal sum from its children, making sure not to calculate the sum for any root more
# than once.  We achieve this by memoizing the maximal sum down from each node once
# it is calculated for the first time. 

# to get command line arguments
import sys
from readPyramid import *

# define global matrix for memoizing
maximalSums = []

############### Supporting Function #################
# find the maximal sum for a particular node in the pyramid
# whose row/column coordinates are defined.
# column cannot be greater than row, as pyramid is stored as a lower triangular matrix
def findMaximalSum(pyramidArray, pyramidSize, row, column):
	if maximalSums[row][column]:
		# if we have already calculated the value for this node
		return maximalSums[row][column]
	else:
		# else we need gets maximal sums for children
		if row == pyramidSize - 1:
			# on last row, just return the node value itself
			return pyramidArray[row][column]
		else:
			# get maximal sums using either child node and return the larger of the two
			leftMaximalSum = pyramidArray[row][column] + findMaximalSum(pyramidArray, pyramidSize, row+1, column)
			rightMaximalSum = pyramidArray[row][column] + findMaximalSum(pyramidArray, pyramidSize, row+1, column+1)
			if leftMaximalSum > rightMaximalSum:
				return leftMaximalSum
			else:
				return rightMaximalSum

#################################################
####### Start main code ########
# read the pyramid of numbers from the input file
pyramidArray = readTriangle(sys.argv[1])

# get pyramid size (number or rows/ number of numbers in the last row)
pyramidSize = len(pyramidArray)

# create matrix to memoize maximal sums
# value set to 0 if maximal sum not saved for the node yet
# The above the diagonal part of the matrix provides no benefit except ease of code
maximalSums =  [[0 for col in range(pyramidSize)] for row in range(pyramidSize)]

maximalSumForPyramid = findMaximalSum(pyramidArray, pyramidSize, 0, 0)
print "Maximal Sum for a path from the top to the bottom of the pyramid is ", maximalSumForPyramid
