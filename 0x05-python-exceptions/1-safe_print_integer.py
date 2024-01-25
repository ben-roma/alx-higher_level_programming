#!/usr/bin/python3

def safe_print_integer(value):
    """Attempts to print an integer using "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        True if the value was successfully printed as an int, False otherwise.
    """

    try:
        print("{:d}".format(value))  # Attempt to print as an integer
        return True  # Indicate successful printing
    except (ValueError, TypeError):
        return False  # Indicate non-integer value
