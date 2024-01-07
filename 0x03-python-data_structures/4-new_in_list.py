#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a copy of a list at a specific position,
    handling out-of-range and negative indices.

    Args:
        my_list: The list to copy and modify.
        idx: The index of the element to replace.
        element: The new element to insert.

    Returns:
        A new list with the element replaced, or a copy of the original
        list if the index is out of range or negative.
    """

    if idx < 0 or idx >= len(my_list):
        return my_list[:]
    else:
        new_list = my_list[:]  # Create a copy of the list
        new_list[idx] = element  # Replace the element in the copy
        return new_list  # Return the modified copy
