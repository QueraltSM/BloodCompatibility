from time import time
import sys
import bloodcomp

showTime = False

if sys.argv[2] == "-t":
    showTime = True
    startTime = time()

persons = open(sys.argv[1], "r").read().split("\n")
bloodcomp.get_combinations(persons)

if showTime:
    print ""
    print "Total execution time:", (time() - startTime) * 1000, "milliseconds"
