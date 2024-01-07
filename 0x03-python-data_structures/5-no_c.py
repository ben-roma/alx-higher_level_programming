#!/usr/bin/python3
def no_c(my_string):
    """Removes all characters 'c' and 'C' from a string.

    Args:
        my_string: The string to modify.

    Returns:
        The new string without 'c' or 'C' characters.
    """

    new_string = ""
    for char in my_string:
        if char not in "cC":  # Check if the character is not 'c' or 'C'
            new_string += char  # Append it to the new string
    return new_string
