#!/usr/bin/python3

    
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        raise TypeError("roman_string must be a string")

    roman_numeral_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    total = 0
    prev = 0  
    for char in roman_string:
        current = roman_numeral_map[char]
        if prev < current:
            total -= 2 * prev
        total += current
        prev = current
    return total

    