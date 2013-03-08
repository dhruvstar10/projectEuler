# a solution to problem 28 of project euler
# http://projecteuler.net/problem=28
# find the sum of the numbers on the diagonal of a spiral
# formed by starting with 1 at the center and moving to the right in a clockwise way
# For the below 5x5 spiral, sum is 101
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
# find it for a 1001x1001 spiral

# strategy - start at the center, progressively add a layer and the sum for that layer

spiralSum = 1                   # starting sum, from center
layerIndex = 0                  # initially, we are at the 0th layer
matrixLengthLeft = 1001 - 1     # we are going through 1001 rows/cols of the matrix. Adding a layer takes 2 of this number

# numbers on the diagonal for the current layer, starting from the south-east corner, going clockwise
(se, sw, nw, ne) = 1, 1, 1, 1

while matrixLengthLeft > 0:    # go through each layer/loop of the spiral, add numbers on the diagonal to the sum
    # starting with a new layer
    layerIndex += 1
    # length of the side of a current layer
    layerLength = (2*layerIndex) + 1
    
    # calculate new values for diagonal end points
    se = ne + layerLength - 1
    sw = se + layerLength - 1
    nw = sw + layerLength - 1
    ne = nw + layerLength - 1

    # add these to the sum
    spiralSum += se + sw + nw + ne


    # done with this layer, reduce the number of iterations left
    matrixLengthLeft -= 2

print "Sum of diagonals of spiral is", spiralSum