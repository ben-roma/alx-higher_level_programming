#!/usr/bin/python3
def common_elements(set_1, set_2):
    """Returns a new set containing the common elements of two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A new set containing the elements that are present in both input sets.
    """

    return set_1.intersection(set_2)
