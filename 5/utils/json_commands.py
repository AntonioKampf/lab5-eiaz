import json


def replace_space(text: str):
    return text.replace('_', ' ')

def remove_key_from_json(key):
    key = replace_space(key)
    with open('./json_files/commands.json', 'r') as file:
        data = json.load(file)
    if key in data:
        del data[key]
    with open('./json_files/commands.json', 'w') as file:
        json.dump(data, file, indent=4)

def add_key_value_to_json(key, value):
    key, value = replace_space(key), value.replace(' ', '_')
    with open('./json_files/commands.json', 'r') as file:
        data = json.load(file)
    data[key] = value
    with open('./json_files/commands.json', 'w') as file:
        json.dump(data, file, indent=4)

def read_json() -> dict:
    with open('./json_files/commands.json', 'r') as file:
        data = json.load(file)
    return data
