#!/usr/bin/env python3

def print_fibonacci(length):
    my_list=[0, 1]
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        return
    # elif length == 2:
    #     print ([0, 1])
    for i in range(2, length):
        next_number = my_list[i-1] + my_list[i-2]
        my_list.append(next_number)

    print (my_list)