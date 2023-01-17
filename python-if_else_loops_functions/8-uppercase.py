#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if i == '\0':
            break
        a = ord(i)
        if a > 96:
            i = chr(a-32)
        print("{}".format(i), end="")
    print("\n")
