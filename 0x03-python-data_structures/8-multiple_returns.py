#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    a = (length, first)
    return tuple(a)
