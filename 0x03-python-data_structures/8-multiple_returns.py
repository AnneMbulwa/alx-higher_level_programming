#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == "":
        return (None)
    return (len(sentence), sentence[0])
