import sys


sys.path.append("..")

from tkinter import Frame, Tk
import pytest

from functions.create_data_entry_form import create_data_entry_form

def app_and_frame():
    root = Tk()
    frame = Frame(root)
    yield root, frame
    root.destroy()
    

#Test if the "add data" button invokes the add_data_to_json function
def test_create_data_entry_form_add_button_works(app_and_frame, mocker):
    root, frame = app_and_frame
    add_data_mock = mocker.patch("functions.create_data_entry")
    create_data_entry_form(root, frame)
    add_button = frame.grid_slaves(row=13, column=0)[0]
    add_button.invoke()
    add_data_mock.assert_called_once()