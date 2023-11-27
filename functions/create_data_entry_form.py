from tkinter import *
from tkinter import messagebox

from functions.add_data_to_json import add_data_to_json

class CreateDataEntryFormBase:
    def __init__(self, app, frame):
        self.app = app
        self.frame = frame
        
        self.company_entry = Entry(self.frame)
        self.datetime_entry = Entry(self.frame)
        self.duration_entry = Entry(self.frame)
        self.phone_entry = Entry(self.frame)
        self.address_entry = Entry(self.frame)
        self.price_entry = Entry(self.frame)
        self.remaining_seats_entry = Entry(self.frame)
        self.total_seats_entry = Entry(self.frame)
        self.age_limit_entry = Entry(self.frame)
        self.outdoor_indoor_entry = Entry(self.frame)
        self.rating_entry = Entry(self.frame)
        self.type_entry = Entry(self.frame)
        self.description_entry = Entry(self.frame)

        fields = [
            ("Company", 0, self.company_entry),
            ("Date and Time", 1, self.datetime_entry),
            ("Duration", 2, self.duration_entry),
            ("Phone", 3, self.phone_entry),
            ("Address", 4, self.address_entry),
            ("Price", 5, self.price_entry),
            ("Remaining Seats", 6, self.remaining_seats_entry),
            ("Total Seats", 7, self.total_seats_entry),
            ("Age Limit", 8, self.age_limit_entry),
            ("Outdoor/Indoor", 9, self.outdoor_indoor_entry),
            ("Rating", 10, self.rating_entry),
            ("Type", 11, self.type_entry),
            ("Description", 12, self.description_entry),
        ]
        
        for field, row, entry_widget in fields:
            label = Label(self.frame, text=field)
            label.grid(row=row, column=0, padx=10, pady=5)
            entry_widget.grid(row=row, column=1, padx=10, pady=5) 
        
            if field == "Remaining Seats" or field == "Total Seats":
                entry_widget.insert(0, "0")
            elif field == "Rating":
                entry_widget.insert(0, "0.0")
                
        def check_empty_widgets(*widgets):
            for widget in widgets:
                if widget.get().strip() == "":
                    return True
            return False
                
        self.add_button = Button(self.frame, text="Legg til data", command=lambda: add_data_to_json(
            self.company_entry, 
            self.datetime_entry, 
            self.duration_entry, 
            self.phone_entry, 
            self.address_entry, 
            self.price_entry,
            self.remaining_seats_entry, 
            self.total_seats_entry, 
            self.age_limit_entry, 
            self.outdoor_indoor_entry,
            self.rating_entry, 
            self.type_entry, 
            self.description_entry
            ) if not check_empty_widgets(
                self.company_entry, 
                self.datetime_entry, 
                self.duration_entry, 
                self.phone_entry, 
                self.address_entry, 
                self.price_entry,
                self.remaining_seats_entry, 
                self.total_seats_entry, 
                self.age_limit_entry, 
                self.outdoor_indoor_entry,
                self.rating_entry, 
                self.type_entry, 
                self.description_entry
            ) else messagebox.showerror("Feil", "Fyll ut alle feltene"))
        self.add_button.grid(row=13, column=0, columnspan=2, padx=10, pady=10)

        self.back_button = Button(self.frame, text="Tilbake", command=lambda: self.app.switch_to_main_frame())
        self.back_button.grid(row=15, column=0, columnspan=2, padx=10, pady=10)