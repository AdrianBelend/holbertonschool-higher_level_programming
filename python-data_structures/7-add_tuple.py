#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    str = [0, 0]
    if len(tuple_a) < 2:
        tuple_c = tuple_a + (0, 0)
        for i in range(2):
            str[i] = tuple_c[i] + tuple_b[i]
    elif len(tuple_b) < 2:
        tuple_c = tuple_b + (0, 0)
        for i in range(2):
            str[i] = tuple_a[i] + tuple_c[i]
    else:
        for i in range(2):
            str[i] = tuple_a[i] + tuple_b[i]
    return(str)
