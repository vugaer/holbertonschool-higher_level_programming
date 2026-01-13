#!/usr/bin/env python3
"""Pickling custom class example."""

import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Returns:
            The filename on success, or None on error.
        """
        with open(filename, "wb") as f:
            pickle.dump(self, f)  # write object in binary mode [web:55]
        return filename

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an instance of CustomObject from a file.

        Returns:
            CustomObject instance on success, or None on error"""

            with open(filename, "rb") as f:
                obj = pickle.load(f)  # load object from binary file [web:55]
            # Ensure the loaded object is actually a CustomObject
            if isinstance(obj, cls):
                return obj
            return None
