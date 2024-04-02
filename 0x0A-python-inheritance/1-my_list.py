#!/usr/bin/python3
"""
Module 1-my_list.
Defines a subclass MyList that inherits from the built-in list class.
Includes a method to print the list in ascending order.
"""


class MyList(list):
    """Inherits from list, adding a method to print it sorted."""

    def print_sorted(self):
        """Prints the list in ascending order
        without altering the original list."""
        print(sorted(self))
