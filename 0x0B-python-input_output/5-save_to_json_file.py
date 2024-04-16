#!/usr/bin/python3
"""
Contains the "from_json_string" function
"""

import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a Json represntation"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
