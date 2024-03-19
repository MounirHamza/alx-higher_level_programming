#!/usr/bin/python3
def multiple_returns(sentence):
    new_tuple = tuple(sentence)
    if len(new_tuple) == "":
        return (0, "None")
    else:
        return (len(new_tuple), new_tuple[0])
