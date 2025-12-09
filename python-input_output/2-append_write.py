#!/usr/bin/python3
"""
Module that contains a function to append text to files.

This module provides functionality for appending strings to UTF-8 encoded
text files and returning the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a UTF-8 text file.

    The function creates the file if it doesn't exist and appends
    the text to the end of the file if it already exists.

    Args:
        filename (str): The path to the file to append. Defaults to empty.
        text (str): The text content to append to the file. Defaults to empty.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
