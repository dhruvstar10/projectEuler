# solution to problem 31 of project euler
# http://projecteuler.net/problem=31
# Find the number of ways to make 200 pence using
# coins of denomination 1,2,5,10,20,50,100,200

# recursive approach
# number of ways to make x using [a < b < c]
# = number of ways to make x-c using [a < b < c]
# + number of ways to make x using [a < b]
# this will have some repitive calculations, which can be avoided by memoization
# not needed for such a small problem

# array of all possible denominations
allDenominations = [1,2,5,10,20,50,100,200]

# function to find the number of combinations
# for a given value and available denominations
# it is expected that allDenominations is a sorted array
# denIndex then represents the max index of allDenominations available in the current recursion
def numCombinations(value, denIndex):
    if value == 0:
        # base case - 1 way to make 0, choose no coins
        return 1
    if denIndex < 0 or value < 0:
        # no possible combination can make value in this case
        return 0
    
    # recursive case - calculate from sub problems
    return numCombinations(value - allDenominations[denIndex], denIndex) + numCombinations(value, denIndex - 1)

print "Number of possible combinations is ", numCombinations(200, len(allDenominations)-1)