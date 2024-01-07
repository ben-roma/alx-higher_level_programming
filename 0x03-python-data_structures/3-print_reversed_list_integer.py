#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order, one per line.

    Args:
        my_list: A list of integers.
    """
    if isinstance(my_list, list):
        my_list.reverse()
        for x in my_list:
            print("{:d}".format(x))
