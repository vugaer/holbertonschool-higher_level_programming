#!/usr/bin/python3
"""Module for writing text to files."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return character count."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
