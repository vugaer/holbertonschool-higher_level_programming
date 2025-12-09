#!/usr/bin/python3
"""
Module that contains a function to write text to files.

This module provides functionality for writing strings to UTF-8 encoded
text files and returning the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Write a string to a UTF-8 text file and return the number of characters.

    The function creates the file if it doesn't exist and overwrites
    the content if the file already exists.

    Args:
        filename (str): The path to the file to write. Defaults to empty string.
        text (str): The text content to write to the file. Defaults to empty.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
