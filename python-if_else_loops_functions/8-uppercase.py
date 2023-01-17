#!/usr/bin/python3
def uppercase(str):
    for i in str:
        a = ord(i)
        if a > 96:
            i = chr(a-32)
        print("{}".format(i), end="")
    print("\n")
