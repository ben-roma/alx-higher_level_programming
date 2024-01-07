#!/usr/bin/python
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers, one row per line,
    with spaces between elements.

    Args:
        matrix: A list of lists representing the matrix.
    """

    for row in matrix:  # Iterate through each row
        for element in row:  # Iterate through each element in the row
            print("{:d} ".format(element), end="")
            # Print the element with a space
        print()
        # Move to the next line after each row
