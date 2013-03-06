# a solution to problem 22 of project euler
# http://projecteuler.net/problem=22
# read a list of names from an input file, sort them, calculate word score based on position
# and add all the word scores. Return the sum.

# to read command line arguments
import sys

###### Helper method for file IO ###############
def readNames(inputFile):
    print "Reading from", inputFile
    f = open(inputFile) # open inputFile in readMode
    nameString = f.read()   # careful, entire file is read (file cannot be large)
    # get rid of quotes, use comma as delimiter and break into array, and return
    return nameString.replace('"', '').split(',')

###### Helper method to get string score of a string, irrespective of position ########
def stringScore(string):
    # get the array with scores of each character in the string
    # ord('A') = 65, the ASCII value of A. Assuming that the input file is all upper case
    scoreArray = map((lambda x: x-64), map(ord, string))
    return sum(scoreArray)  # return the score for the current string


#################################################
####### Start main code ########
# read input file and get list of names in an array
namesArray = readNames(sys.argv[1])
namesArray.sort()   # sort the list of names

sumNameScore = 0    # initialize the sum of all name scores in file
for i in range(len(namesArray)):  # go over each string, find positional score, and add to sum
    sumNameScore += (i+1)*stringScore(namesArray[i])

# output result
print "Name Score is ", sumNameScore