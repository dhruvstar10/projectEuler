# a solution to problem 32 of project euler
# http://projecteuler.net/problem=32
# find all 1-9 pandigital products and find their sum
# multiplicand/multiplier/product combo contains each digit from 1-9 exactly once

# a clever solution might be to find all combinations/permutations of 1-9
# and then check how many of them satisfy a*b = c.  However, a brute force would
# quicker and faster

pandigitalSum = 0   # sum of all pandigital combos
productArray = []   # keep track of pandigital products to avoid duplication
                    # assumes that a pandigital product corresponds to exactly one combo

# in the following code
# x = multiplicand
# y = multiplier
# z = product
# x * y = z
for x in range(1, 9877):
    # need to check only 4 digit multiplicands at most
    # 5 digit multiplicands would imply at least 5 digits in the product
    # and then the combo would have more than 9 digits, which is not allowed

    # convert the number to an array of its constituent digits
    xArr = list(str(x))
    # weed out x's with duplicate digits, as pandigital products require unique digits
    # set of array is array of unique elements in it
    # also weed out x's with 0's in them
    if not '0' in xArr and len(xArr) == len(set(xArr)):
        # now we are going to check y's for the current x
        # need to check at most 1 and 2 digit y's
        for y in range(1, 99):
            # convert y into array of digits
            yArr = list(str(y))
            z = x * y     # get z
            zArr = list(str(z)) # convert to array of digits

            # merge all the arrays and check if pandigital
            comboArr = xArr + yArr + zArr
            if not '0' in comboArr and len(comboArr) == 9 and len(set(comboArr)) == 9 and not z in productArray:
                # this is a pandigital combo
                pandigitalSum += z
                productArray.append(z)

# output result
print "Sum of all pandigital combos is ", pandigitalSum