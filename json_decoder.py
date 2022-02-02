import json
import sys
import os
import platform


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def load_json(filepath):
    with open(filepath, "r") as file:
        return json.load(file)


def get_entries(data):
    return [entry["entryName"] for entry in data["entries"]]


def get_exits(data, entry):
    return [exit for exit in data["entries"][entry]["exits"]]


def get_skill_value(data):
    return [value["value"] for value in data["skills"]]

vault_path = (
    resource_path("data/vaults.json")
    if platform.system() == "Linux"
    else resource_path("data\\vaults.json")
)
skills_path = (
    resource_path("data/test.json")
    if platform.system() == "Linux"
    else resource_path("data\\test.json")
)
