#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list in reverse order, one per line.

    Args:
        my_list: A list of integers.
    """

    for i in range(len(my_list) - 1, -1, -1):  # Iterate in reverse order
        print("{:d}".format(my_list[i]))  # Print each integer on a line
