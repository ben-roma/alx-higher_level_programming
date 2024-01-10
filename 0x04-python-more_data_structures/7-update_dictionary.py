def update_dictionary(a_dictionary, key, value):
    """Updates a dictionary by adding or replacing a key-value pair.

    Args:
        a_dictionary: The dictionary to update.
        key: The key to add or update.
        value: The value to associate with the key.

    Returns:
        The updated dictionary.
    """

    a_dictionary[key] = value
    return a_dictionary
