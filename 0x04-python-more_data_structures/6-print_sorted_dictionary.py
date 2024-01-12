#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sort_list = sorted(a_dictionary.keys())
    for key in sort_list:
        value = a_dictionary[key]
        print(f"{key}: {value}")
