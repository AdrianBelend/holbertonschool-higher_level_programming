#!/usr/bin/python3
def max_integer(my_list=[]):
    a = -1000
    if my_list == []:
        return(None)
    else:
        for i in my_list:
            if i > a:
                a = i
        return(a)
