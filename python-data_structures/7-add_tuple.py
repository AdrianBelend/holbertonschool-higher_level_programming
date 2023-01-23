#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) >= len(tuple_b):
        tuple_c = tuple_b + (0, 0)
        str = [0] * len(tuple_a)
        for i in range(len(tuple_a)):
            str[i] = tuple_a[i] + tuple_c[i]
    else:
        str = [0] * len(tuple_b)
        tuple_c = tuple_a + (0, 0)
        for i in range(len(tuple_b)):
            str[i] = tuple_a[i] + tuple_b[i]
    return(str)
