from tkinter import Button, Entry, Frame, Tk
import pytest

from functions.create_data_entry_form import CreateDataEntryFormBase

@pytest.fixture
def create_data_entry_form():
    root = Tk()
    frame = Frame(root)
    data_entry_form = CreateDataEntryFormBase(root, frame)
    return data_entry_form

#WIDGETS:

#Testing the widgets to check if they are created.
def test_is_create_data_entry_form_widgets_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.company_entry, Entry)
    assert isinstance(create_data_entry_form.datetime_entry, Entry)
    assert isinstance(create_data_entry_form.duration_entry, Entry)
    assert isinstance(create_data_entry_form.phone_entry, Entry)
    assert isinstance(create_data_entry_form.address_entry, Entry)
    assert isinstance(create_data_entry_form.price_entry, Entry)
    assert isinstance(create_data_entry_form.remaining_seats_entry, Entry)
    assert isinstance(create_data_entry_form.total_seats_entry, Entry)
    assert isinstance(create_data_entry_form.age_limit_entry, Entry)
    assert isinstance(create_data_entry_form.outdoor_indoor_entry, Entry)
    assert isinstance(create_data_entry_form.rating_entry, Entry)
    assert isinstance(create_data_entry_form.type_entry, Entry)
    assert isinstance(create_data_entry_form.description_entry, Entry)
    
#Testing to see if the buttons are created
def test_is_create_data_entry_form_buttons_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.add_button, Button)
    assert isinstance(create_data_entry_form.back_button, Button)

#Testing default values
def test_default_values(create_data_entry_form):
    assert create_data_entry_form.remaining_seats_entry.get() == "0"
    assert create_data_entry_form.total_seats_entry.get() == "0"
    assert create_data_entry_form.rating_entry.get() == "0.0"