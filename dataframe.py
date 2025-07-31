import json
import pandas as pd

def read_json_as_string(file_path):
    with open(file_path, 'r') as file:
        json_string = file.read()
    return json_string

