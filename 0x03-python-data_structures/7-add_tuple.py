#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two tuples element-wise, handling different lengths
    and returning a tuple with the first two sums.

    Args:
        tuple_a: The first tuple.
        tuple_b: The second tuple.

    Returns:
        A tuple containing the sum of the first two elements of each tuple.
    """

    first_elements = (tuple_a + (0, 0))[:2]
    second_elements = (tuple_b + (0, 0))[:2]
    return (first_elements[0] + second_elements[0],
            first_elements[1] + second_elements[1])
