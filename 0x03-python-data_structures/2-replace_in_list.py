#!/usr/python3

def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position,
    handling out-of-range and negative indices.

    Args:
        my_list: The list to modify.
        idx: The index of the element to replace.
        element: The new element to insert.

    Returns:
        The modified list, or the original list if the index is out
        of range or negative.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list  # Return original list for invalid indices
    else:
        my_list[idx] = element  # Replace the element at the specified index
        return my_list  # Return the modified list
