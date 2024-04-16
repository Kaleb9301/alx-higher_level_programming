#!/usr/bin/python3
"""
Contains the "to_json_string" function
"""

import json


def to_json_string(my_obj):
    """returns the JSON representation of object (string)"""
    return json.dumps(my_obj)
