#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = tuple(sentence)
    if len(new_tuple) == 0:
        return "None"
    else:
        return len(new_tuple), new_tuple[0]
