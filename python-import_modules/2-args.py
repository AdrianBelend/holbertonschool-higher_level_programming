#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
a = 0
print("{} arguments:".format(len(argv) - 1))

for i in range(1, len(argv)):
    a = a + 1
    print("{}: {}".format(a, argv[i]))
