#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a new set containing elements present in only one of the sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A new set containing elements that are present in either
        set_1 or set_2, but not in both."""

    return (set_1 ^ set_2)  # Efficiently use the symmetric difference operator
