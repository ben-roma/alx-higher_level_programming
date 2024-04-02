#!/usr/bin/python3
"""
Module 0-lookup.
Defines a function that returns a list of available attributes
and methods of an object.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: Any object.

    Returns:
        A list object containing the names of the attributes and methods.
    """
    return dir(obj)
