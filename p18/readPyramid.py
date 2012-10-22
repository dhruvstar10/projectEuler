# a util file to read a pyramid/triangle of numbers and convert it to a an array of arrays

def readTriangle(inputFile):
	print "Reading from", inputFile
	with open(inputFile) as f:
		pyramidArray = [] # array to store data from file
		for line in f: # read lines
			# for each line in the file, add it to the array
        		pyramidArray.append([int(x) for x in line.split()])
	return pyramidArray
