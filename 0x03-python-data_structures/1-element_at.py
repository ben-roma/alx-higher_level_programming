#!/usr/python

def element_at(my_list, idx):
    """Retrieves an element from a list, handling out-of-range and negative indices.

    Args:
        my_list: The list to access.
        idx: The index of the element to retrieve.

    Returns:
        The element at the specified index, or None if the index is out of range or negative.
    """

    if idx < 0 or idx >= len(my_list):
        return None  # Return None for invalid indices
    else:
        return my_list[idx]  # Access and return the element
