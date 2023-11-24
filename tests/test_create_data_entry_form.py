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

#Testing to see if the company_entry widget is created
def test_is_create_data_entry_form_company_entry_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.company_entry, Entry)

#Testing to see if the datetime_entry widget is created
def test_is_create_data_entry_form_duration_entry_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.datetime_entry, Entry)

#Testing to see if the duration_entry widget is created
def test_is_create_data_entry_form_duration_duration_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.duration_entry, Entry)

#Testing to see if the phone_entry widget is created
def test_is_create_data_entry_form_duration_phone_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.phone_entry, Entry)

#Testing to see if the address_entry widget is created
def test_is_create_data_entry_form_duration_address_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.address_entry, Entry)

#Testing to see if the price_entry widget is created
def test_is_create_data_entry_form_duration_price_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.price_entry, Entry)

#Testing to see if the remaining_seats_entry widget is created
def test_is_create_data_entry_form_duration_remaining_seats_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.remaining_seats_entry, Entry)
   
#Testing to see if the total_seats_entry widget is created 
def test_is_create_data_entry_form_duration_total_seats_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.total_seats_entry, Entry)

#Testing to see if the age_limit_entry widget is created    
def test_is_create_data_entry_form_duration_age_limit_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.age_limit_entry, Entry)

#Testing to see if the outdoor_indoor_entry widget is created   
def test_is_create_data_entry_form_duration_outdoor_indoor_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.outdoor_indoor_entry, Entry)

#Testing to see if the rating_entry widget is created   
def test_is_create_data_entry_form_duration_rating_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.rating_entry, Entry)
    
#Testing to see if the type_entry widget is created
def test_is_create_data_entry_form_duration_type_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.type_entry, Entry)
    
#Testing to see if the description_entry widget is created
def test_is_create_data_entry_form_duration_description_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.description_entry, Entry)
    
#Testing to see if the add_button are created
def test_is_create_data_entry_form_add_button_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.add_button, Button)

#Testing to see if the back_button are created 
def test_is_create_data_entry_form_back_button_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.back_button, Button)

#Testing default values

#Testing to see if the remaining_seats widget contains the default value of 0, when not set.
def test_is_create_data_entry_form_remaining_seats_entry_widget_default_value(create_data_entry_form):
    assert create_data_entry_form.remaining_seats_entry.get() == "0"

#Testing to see if the total_seats_entry widget contains the default value of 0, when not set.
def test_is_create_data_entry_form_total_seats_entry_widget_default_value(create_data_entry_form):
    assert create_data_entry_form.total_seats_entry.get() == "0"

#Testing to see if the rating_entry widget contains the default value of 0, when not set.
def test_is_create_data_entry_form_rating_entry_widget_default_value(create_data_entry_form):
    assert create_data_entry_form.rating_entry.get() == "0.0"