import tkinter as tk

from functions.add_data_to_json import add_data_to_json

def create_data_entry_form():    
    window = tk.Tk()
    window.title("Data Form")
    
    company_entry = tk.Entry(window)
    datetime_entry = tk.Entry(window)
    duration_entry = tk.Entry(window)
    phone_entry = tk.Entry(window)
    address_entry = tk.Entry(window)
    price_entry = tk.Entry(window)
    remaining_seats_entry = tk.Entry(window)
    total_seats_entry = tk.Entry(window)
    age_limit_entry = tk.Entry(window)
    outdoor_indoor_entry = tk.Entry(window)
    rating_entry = tk.Entry(window)
    type_entry = tk.Entry(window)
    description_entry = tk.Entry(window)
    
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
        label = tk.Label(window, text=field)
        label.grid(row=row, column=0, padx=10, pady=5)
        entry_widget.grid(row=row, column=1, padx=10, pady=5) 
    
        if field == "Remaining Seats" or field == "Total Seats":
            entry_widget.insert(0, "0")
        elif field == "Rating":
            entry_widget.insert(0, "0.0")
            
    add_button = tk.Button(window, text="Add Data", command=lambda: add_data_to_json(
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
    
    window.mainloop()