from tkinter import *

from functions.add_data_to_json import add_data_to_json
#from main_application import MainApplication

class CreateDataEntryFormBase:
    def __init__(self, app, frame):
        self.app = app
        self.frame = frame
        self.create_data_entry_form()
        
    def create_data_entry_form(self):   
        company_entry = Entry(self.frame)
        datetime_entry = Entry(self.frame)
        duration_entry = Entry(self.frame)
        phone_entry = Entry(self.frame)
        address_entry = Entry(self.frame)
        price_entry = Entry(self.frame)
        remaining_seats_entry = Entry(self.frame)
        total_seats_entry = Entry(self.frame)
        age_limit_entry = Entry(self.frame)
        outdoor_indoor_entry = Entry(self.frame)
        rating_entry = Entry(self.frame)
        type_entry = Entry(self.frame)
        description_entry = Entry(self.frame)
        
        fields = [
            ("Company", 0, company_entry),
            ("Date and Time", 1, datetime_entry),
            ("Duration", 2, duration_entry),
            ("Phone", 3, phone_entry),
            ("Address", 4, address_entry),
            ("Price", 5, price_entry),
            ("Remaining Seats", 6, remaining_seats_entry),
            ("Total Seats", 7, total_seats_entry),
            ("Age Limit", 8, age_limit_entry),
            ("Outdoor/Indoor", 9, outdoor_indoor_entry),
            ("Rating", 10, rating_entry),
            ("Type", 11, type_entry),
            ("Description", 12, description_entry),
        ]
        
        for field, row, entry_widget in fields:
            label = Label(self.frame, text=field)
            label.grid(row=row, column=0, padx=10, pady=5)
            entry_widget.grid(row=row, column=1, padx=10, pady=5) 
        
            if field == "Remaining Seats" or field == "Total Seats":
                entry_widget.insert(0, "0")
            elif field == "Rating":
                entry_widget.insert(0, "0.0")
                
        add_button = Button(self.frame, text="Add Data", command=lambda: add_data_to_json(
            company_entry, 
            datetime_entry, 
            duration_entry, 
            phone_entry, 
            address_entry, 
            price_entry,
            remaining_seats_entry, 
            total_seats_entry, 
            age_limit_entry, 
            outdoor_indoor_entry,
            rating_entry, 
            type_entry, 
            description_entry
            ))
        add_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

        back_button = Button(self.frame, text="Back", command=lambda: self.app.switch_to_main_frame())
        back_button.grid(row=15, column=0, columnspan=2, padx=10, pady=10)