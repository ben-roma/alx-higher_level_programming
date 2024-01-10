#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Creates a new list with all occurrences of
    `search` replaced by `replace`.

    Args:
        my_list: The original list.
        search: The element to replace.
        replace: The new element to insert.

    Returns:
        A new list with the replacements made.
    """

    new_list = []
    for item in my_list:
        new_list.append(replace if item == search else item)
    return new_list
