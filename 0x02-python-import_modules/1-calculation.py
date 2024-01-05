#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

addresult = add(a, b)
subresult = sub(a, b)
mulresult = mul(a, b)
divresult = div(a, b)

print("{} + {} = {}".format(a, b, addresult))
print("{} - {} = {}".format(a, b, subresult))
print("{} * {} = {}".format(a, b, mulresult))
print("{} / {} = {}".format(a, b, divresult))
