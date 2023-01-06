import sys
import getopt
import argparse

#allows user to pass in file path, if file is not present then print helpstring
try:
    args, options = getopt.getopt(sys.argv[1:], "o", ["orgs="])
except:
    print("invalid input")

for 