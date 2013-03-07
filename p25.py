# A solution to problem 25 of project euler
# http://projecteuler.net/problem=25
# Output the first 1000 digit Fibonacci number

from util import *

fibArray = [0, 1]   # initialize the array of fibonacci numbers, such that fibArray[i] will be the ith fibonacci number
curFibAmount = 1    # current size of fib array, implying that we have 1 fibonacci number right now

# for performance reasons, we will generate a set of fibonacci number, and then query the length
# we will initially start by generating a set of 100 numbers, and keep on increasing the size of the incremental set
generateSetCount = 100

foundAnswer = False # bool to check if we have the answer
while not foundAnswer:
    desiredFibAmount = curFibAmount + generateSetCount  # generate the next set of Fibonacci numbers
    while curFibAmount < desiredFibAmount:
        curFibAmount += 1
        newFibNum = fibArray[curFibAmount - 1] + fibArray[curFibAmount - 2]     # calculate the next fibonacci number
        fibArray.append(newFibNum)                                              # add it to the list

    if numDigits(fibArray[curFibAmount]) >= 1000:   # have already generated the answer
        foundAnswer = True
    else:
        generateSetCount *= 2   # increase the number of numbers that will be generated next time

# so now we know that fibArray[curFibAmount] has more than 1000 digits.
# Do a binary search to find the first 1000 digit fibonacci number
endIndex = curFibAmount
startIndex = curFibAmount - generateSetCount
while numDigits(fibArray[startIndex]) < 1000:
    midIndex = (startIndex + endIndex)/2
    if numDigits(fibArray[midIndex]) < 1000:
        startIndex = midIndex + 1
    else:
        endIndex = midIndex

# print Output
print "The First 1000 digit Fibonacci number is ",startIndex,"th number"