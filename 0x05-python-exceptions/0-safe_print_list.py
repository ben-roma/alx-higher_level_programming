#!/bin/usr/python3

def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list, handling potential IndexError exceptions.

    Args:
        my_list: The list to print elements from.
        x: The number of elements to print.

    Returns:
        The actual number of elements printed.
    """

    printed_count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")  # Print elements without newline
            printed_count += 1
    except IndexError:
        pass  # Silently handle IndexError if x exceeds list length
    print()  # Add a newline after printing elements
    return printed_count
