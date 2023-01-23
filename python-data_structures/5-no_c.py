#!/usr/bin/python3
def no_c(my_string):
    a = 0
    new_string = ''
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            new_string = my_string[0: i - a] + my_string[(i + 1):]
            a = a + 1
    return(new_string)
