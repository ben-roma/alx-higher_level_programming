#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints the key-value pairs of dictionary in alphabetical order of keys.

    Args:
        a_dictionary: The dictionary to print.
    """

    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")  # Print each key-value pair
