#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation:

"""


import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file"""
    with open(filename, 'a', encoding='utf-8') as f:
        f.write(json.dumps(my_obj))
