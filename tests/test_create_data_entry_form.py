from tkinter import Button, Entry, Frame, Tk
import pytest

from functions.create_data_entry_form import CreateDataEntryFormBase

@pytest.fixture
def create_data_entry_form():
    root = Tk()
    frame = Frame(root)
    data_entry_form = CreateDataEntryFormBase(root, frame)
    return data_entry_form

def fields_data(create_data_entry_form, position):
    fields = [
        ("Company", position, create_data_entry_form.company_entry),
        ("Date and Time", position, create_data_entry_form.datetime_entry),
        ("Duration", position, create_data_entry_form.duration_entry),
        ("Phone", position, create_data_entry_form.phone_entry),
        ("Address", position, create_data_entry_form.address_entry),
        ("Price", position, create_data_entry_form.price_entry),
        ("Remaining Seats", position, create_data_entry_form.remaining_seats_entry),
        ("Total Seats", position, create_data_entry_form.total_seats_entry),
        ("Age Limit", position, create_data_entry_form.age_limit_entry),
        ("Outdoor/Indoor", position, create_data_entry_form.outdoor_indoor_entry),
        ("Rating", position, create_data_entry_form.rating_entry),
        ("Type", position, create_data_entry_form.type_entry),
        ("Description", position, create_data_entry_form.description_entry),
    ]
    return fields


#WIDGETS:
#Testing the widgets to check if they are created.

#Testing to see if the company_entry widget is created
def test_is_create_data_entry_form_company_entry_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.company_entry, Entry)

#Testing to see if the datetime_entry widget is created
def test_is_create_data_entry_form_datetime_entry_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.datetime_entry, Entry)

#Testing to see if the duration_entry widget is created
def test_is_create_data_entry_form_duration_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.duration_entry, Entry)

#Testing to see if the phone_entry widget is created
def test_is_create_data_entry_form_phone_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.phone_entry, Entry)

#Testing to see if the address_entry widget is created
def test_is_create_data_entry_form_address_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.address_entry, Entry)

#Testing to see if the price_entry widget is created
def test_is_create_data_entry_form_price_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.price_entry, Entry)

#Testing to see if the remaining_seats_entry widget is created
def test_is_create_data_entry_form_remaining_seats_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.remaining_seats_entry, Entry)
   
#Testing to see if the total_seats_entry widget is created 
def test_is_create_data_entry_form_total_seats_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.total_seats_entry, Entry)

#Testing to see if the age_limit_entry widget is created    
def test_is_create_data_entry_form_age_limit_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.age_limit_entry, Entry)

#Testing to see if the outdoor_indoor_entry widget is created   
def test_is_create_data_entry_form_outdoor_indoor_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.outdoor_indoor_entry, Entry)

#Testing to see if the rating_entry widget is created   
def test_is_create_data_entry_form_rating_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.rating_entry, Entry)
    
#Testing to see if the type_entry widget is created
def test_is_create_data_entry_form_type_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.type_entry, Entry)
    
#Testing to see if the description_entry widget is created
def test_is_create_data_entry_form_description_widget_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.description_entry, Entry)
    
#Testing to see if the add_button is created
def test_is_create_data_entry_form_add_button_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.add_button, Button)

#Testing to see if the back_button is created 
def test_is_create_data_entry_form_back_button_created(create_data_entry_form):
    assert isinstance(create_data_entry_form.back_button, Button)

#Testing to check the default values:

#Testing to see if the remaining_seats widget contains the default value of 0, when not set.
def test_is_create_data_entry_form_remaining_seats_entry_widget_default_value(create_data_entry_form):
    assert create_data_entry_form.remaining_seats_entry.get() == "0"

#Testing to see if the total_seats_entry widget contains the default value of 0, when not set.
def test_is_create_data_entry_form_total_seats_entry_widget_default_value(create_data_entry_form):
    assert create_data_entry_form.total_seats_entry.get() == "0"

#Testing to see if the rating_entry widget contains the default value of 0, when not set.
def test_is_create_data_entry_form_rating_entry_widget_default_value(create_data_entry_form):
    assert create_data_entry_form.rating_entry.get() == "0.0"


#Testing to see if the back button contains the right text
def test_is_create_data_entry_form_name_back_button_correct(create_data_entry_form):
    assert create_data_entry_form.back_button.cget("text") == "Tilbake"

#Testing to see if the add data button contains the right text
def test_is_create_data_entry_form_name_add_button_correct(create_data_entry_form):
    assert create_data_entry_form.add_button.cget("text") == "Legg til data"


# Testing the labels in fields, testing if the text is in the right position (0)
def test_company_label_0_is_in_position_0_and_name_is_correct(create_data_entry_form, position=0):

    fields = fields_data(create_data_entry_form, position)
    # Check if the label name contains "Company" and is in the expected position
    label_to_test = fields[position][0]  # Get the label name based on the position
    # Get the Entry widget for the specified label
    entry_widget = fields[position][2]  # Get the corresponding entry widget

    assert "Company" in label_to_test
    assert fields[position][1] == 0  # Ensuring "Company" is in position 0

    # Check if the entry widget is present
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (1)
def test_company_label_1_is_in_position_1_and_name_is_correct(create_data_entry_form, position=1):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Date and Time" in label_to_test
    assert fields[position][1] == 1
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (2)
def test_company_label_2_is_in_position_2_and_name_is_correct(create_data_entry_form, position=2):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Duration" in label_to_test
    assert fields[position][1] == 2
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (3)
def test_company_label_3_is_in_position_3_and_name_is_correct(create_data_entry_form, position=3):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Phone" in label_to_test
    assert fields[position][1] == 3
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (4)
def test_company_label_4_is_in_position_4_and_name_is_correct(create_data_entry_form, position=4):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Address" in label_to_test
    assert fields[position][1] == 4
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (5)
def test_company_label_5_is_in_position_5_and_name_is_correct(create_data_entry_form, position=5):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Price" in label_to_test
    assert fields[position][1] == 5
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (6)
def test_company_label_6_is_in_position_6_and_name_is_correct(create_data_entry_form, position=6):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Remaining Seats" in label_to_test
    assert fields[position][1] == 6
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (7)
def test_company_label_7_is_in_position_7_and_name_is_correct(create_data_entry_form, position=7):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Total Seats" in label_to_test
    assert fields[position][1] == 7
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (8)
def test_company_label_8_is_in_position_8_and_name_is_correct(create_data_entry_form, position=8):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Age Limit" in label_to_test
    assert fields[position][1] == 8
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (9)
def test_company_label_9_is_in_position_9_and_name_is_correct(create_data_entry_form, position=9):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Outdoor/Indoor" in label_to_test
    assert fields[position][1] == 9
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (10)
def test_company_label_10_is_in_position_10_and_name_is_correct(create_data_entry_form, position=10):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Rating" in label_to_test
    assert fields[position][1] == 10
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (11)
def test_company_label_11_is_in_position_11_and_name_is_correct(create_data_entry_form, position=11):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Type" in label_to_test
    assert fields[position][1] == 11
    assert entry_widget.winfo_exists()

# Testing the labels in fields, testing if the text is in the right position (12)
def test_company_label_12_is_in_position_12_and_name_is_correct(create_data_entry_form, position=12):

    fields = fields_data(create_data_entry_form, position)
    label_to_test = fields[position][0]
    entry_widget = fields[position][2]
    assert "Description" in label_to_test
    assert fields[position][1] == 12
    assert entry_widget.winfo_exists()