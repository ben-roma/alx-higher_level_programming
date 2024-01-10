#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds only the unique integers in a list.

    Args:
        my_list: A list of integers.

    Returns:
        The sum of the unique integers in the list.
    """

    seen = set()
    unique_sum = 0
    for num in my_list:
        if num not in seen:
            seen.add(num)
            unique_sum += num
    return unique_sum
