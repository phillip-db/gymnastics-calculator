import json

vault_path = 'data/vaults.json'

def load_vaults(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)

def get_entries(data):
    return [entry for entry in data['entries']]

def get_exits(data, entry):
    return [exit for exit in data['entries'][entry]['exits']]