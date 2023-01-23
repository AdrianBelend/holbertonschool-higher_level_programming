#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == []:
        a = None
    else:
        a = sentence[0]
    tuple = (len(sentence), a)
    return(tuple)
