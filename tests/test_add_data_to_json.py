import json
from tkinter import Button, Entry, Frame, Tk
import pytest
from functions.add_data_to_json import add_data_to_json
from functions.create_data_entry_form import CreateDataEntryFormBase


def test_does_data_get_added_to_json():
    my = {"test"}
    add_data_to_json()
    existing_json_data = []
    with open("json_files/data.json", "r") as file:
        existing_json_data = json.load(file)
    last_entry = existing_json_data[-1]

    assert last_entry["Company"] == "test"
    assert last_entry["Date and Time"] == "test"

    print(last_entry)
