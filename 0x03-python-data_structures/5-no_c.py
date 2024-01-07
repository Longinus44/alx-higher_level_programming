#!/usr/bin/python3
def no_c(my_string):
    return ''.join([word for word in my_string if word.lower() != 'c'])
