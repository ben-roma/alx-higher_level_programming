#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Deletes the item at the specified index in a list
    handling out-of-range cases and avoiding pop().

    Args:
        my_list: The list to modify.
        idx: The index of the item to delete.

    Returns:
        A new list with the item at the specified index removed.
    """
    if idx >= 0 and idx < len(my_list):
        del my_list[idx]
    return my_list
