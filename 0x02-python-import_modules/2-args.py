#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args_len = len(argv) - 1

    print("{} argument{}{}:".format(args_len, 's' if args_len !=
          1 else '', '.' if args_len == 0 else ''))

    for i, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(i, arg))
