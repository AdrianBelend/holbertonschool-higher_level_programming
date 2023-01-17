#!/usr/bin/python3
def pow(a, b):
    c = 1
    d = b
    if b == 0:
        return 1
    if b < 0:
        b = b*-1
    for i in range(0, b):
        c = c * a
    if d < 0:
        c = 1 / c
    return c
