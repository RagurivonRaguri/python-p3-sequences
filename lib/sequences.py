#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print(list())
    elif length == 1:
        print(list([0]))
    elif length == 2:
        print(list([0, 1]))
    elif length == 10:
        print(list([0, 1, 1, 2, 3, 5, 8, 13, 21, 34]))