#!/usr/bin/python3

def multiple_returns(sentence):
    """Returns a tuple containing the length of the sentence
    and its first character, or None if empty.

    Args:
        sentence: The input string.

    Returns:
        A tuple of (length, first_character) or
        (length, None) if the sentence is empty.
    """

    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return length, first_char
