#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """Prints a matrix of integers, one row per line,
    with spaces between elements.

    Args:
        matrix: A list of lists representing the matrix.
    """

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j != 0:
                print(" ", end='')
            print("{:d}".format(matrix[i][j]), end='')
        print()
