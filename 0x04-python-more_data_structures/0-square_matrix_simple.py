#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Returns a new matrix with each element squared,
    leaving the original matrix intact.

    Args:
        matrix: A 2-dimensional list of integers.

    Returns:
        A new matrix with the same dimensions, where each
        element is the square of the corresponding
        element in the input matrix.
    """

    new_matrix = []
    for row in matrix:
        new_row = [item**2 for item in row]
        new_matrix.append(new_row)
    return new_matrix
