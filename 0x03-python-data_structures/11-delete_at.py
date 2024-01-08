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

    if 0 <= idx < len(my_list):  # Check for valid index
        return my_list[:idx] + my_list[idx+1:]
        # Reconstruct list without the element at idx
    else:
        return my_list  # Return original list if index is invalid
