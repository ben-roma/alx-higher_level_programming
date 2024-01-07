#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Prints all integers of a list, one per line.

    Args:
        my_list: A list of integers.
    """

    for integer in my_list:
        print("{:d}".format(integer))  # Print each integer on a separate line
