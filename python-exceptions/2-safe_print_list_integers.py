#!/usr/bin/pyhton3
def safe_print_list_integers(my_list=[], x=0):
    a = 0
    for i in range(x):
        try:
            print("{:d}.format(x)", end="")
            a += 1
        except (ValueError, TypeError):
            continue
        print("")
        return(j)

