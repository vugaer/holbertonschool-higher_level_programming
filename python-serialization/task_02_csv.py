#!/usr/bin/env python3
import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into JSON format and writes it to data.json.

    Args:
        csv_filename (str): Path to the CSV file.

    Returns:
        bool: True if conversion succeeds, False otherwise.
    """
    try:
        with open(csv_filename, "r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = [row for row in reader]

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
