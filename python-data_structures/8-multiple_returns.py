#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == []:
        a = None
    else:
        a = len(sentence)
    tuple = (a, sentence[0])
    return(tuple)
