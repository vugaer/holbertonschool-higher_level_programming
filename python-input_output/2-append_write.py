#!/usr/bin/python3
"""Module for appending text to files."""


def append_write(filename="", text=""):
    """Append a string to a UTF-8 text file and return character count."""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
