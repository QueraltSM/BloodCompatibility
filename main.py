from time import time
import sys
import bloodcomp

if len(sys.argv) < 2:
    print("usage: main.py dataset_file [-t]")
    print("  options: \n"
          "   -t, Execution with time")

elif len(sys.argv) == 2:
    persons = open(sys.argv[1], "r").read().split("\n")
    bloodcomp.get_combinations(persons)

elif sys.argv[2] == "-t":
    startTime = time()
    persons = open(sys.argv[1], "r").read().split("\n")
    bloodcomp.get_combinations(persons)
    elapsedTime = time() - startTime
    print("\nTotal execution time:", elapsedTime * 1000, "milliseconds")
