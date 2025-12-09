#!/usr/bin/python3
"""
Module that contains a function to read and print text files.

This module provides functionality for reading UTF-8 encoded text files
and printing their contents to standard output.
"""


def read_file(filename=""):
    """
    Read a UTF-8 text file and print it to stdout.

    Args:
        filename (str): The path to the file to read. Defaults to empty string.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
