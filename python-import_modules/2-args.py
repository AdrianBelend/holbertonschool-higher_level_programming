#!/usr/bin/python3
import sys
a = 0
for i in range(1, len(sys.argv)):
    a = a + 1
    print("{}: {}".format(a, sys.argv[i]))
