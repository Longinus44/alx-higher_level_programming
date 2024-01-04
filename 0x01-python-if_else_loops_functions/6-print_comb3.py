#!/usr/bin/python3

for i in range(10):
    for p in range(i + 1, 10):
        if i == 8 and p == 9:
            print("{:02d}".format(i * 10 + p))
        else:
            print("{:02d}".format(i * 10 + p), end=", ")
