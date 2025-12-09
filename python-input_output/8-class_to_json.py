#!/usr/bin/python3
"""Module for class to JSON dictionary conversion."""


def class_to_json(obj):
    """Return the dictionary description for JSON serialization of object."""
    return obj.__dict__
