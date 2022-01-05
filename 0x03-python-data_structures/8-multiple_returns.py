#!/usr/bin/python3
def multiple_returns(sentence):
    long = len(sentence)

    if (long == 0):
        new_tuple = (long, None)
    else:
        new_tuple = (long, sentence[0])
    return (new_tuple)
