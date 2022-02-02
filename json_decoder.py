import json

vault_path = 'data/vaults.json'
skills_path = 'data/test.json'

def load_json(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_entries(data):
    return [entry['entryName'] for entry in data['entries']]

def get_exits(data, entry):
    return [exit for exit in data['entries'][entry]['exits']]

def get_skill_value(data):
    return [value['value'] for value in data['skills']]
