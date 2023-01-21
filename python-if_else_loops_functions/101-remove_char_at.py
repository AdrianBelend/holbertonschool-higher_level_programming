#!/usr/bin/python3
def remove_char_at(str, n):
    abc = ""
    for i in range(0,len(str)):
        if i == n:
            continue
        else:
           abc = abc + str[i]
    return(abc)
