import json
from tkinter import END


def add_data_to_json(company_entry,
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
                     description_entry):
    new_json_data = {
        "Company": company_entry.get(),
        "Date and Time": datetime_entry.get(),
        "Duration": duration_entry.get(),
        "Phone": phone_entry.get(),
        "Address": address_entry.get(),
        "Price": price_entry.get(),
        "Available Seats": {
            "Remaining": remaining_seats_entry.get(),
            "Total": total_seats_entry.get()
        },
        "Age Limit": age_limit_entry.get(),
        "Outdoor/Indoor": outdoor_indoor_entry.get(),
        "Rating": rating_entry.get(),
        "Type": type_entry.get(),
        "Description": description_entry.get()
    }

    existing_json_data = []
    try:
        with open("json_files/data.json", "r") as file:
            existing_json_data = json.load(file)
    except FileNotFoundError:
        pass

    existing_json_data.append(new_json_data)

    with open("json_files/data.json", "w") as file:
        json.dump(existing_json_data, file, indent=4)

    print("Data added to the JSON file.")

    company_entry.delete(0, END)
    datetime_entry.delete(0, END)
    duration_entry.delete(0, END)
    phone_entry.delete(0, END)
    address_entry.delete(0, END)
    price_entry.delete(0, END)
    remaining_seats_entry.delete(0, END)
    total_seats_entry.delete(0, END)
    age_limit_entry.delete(0, END)
    outdoor_indoor_entry.delete(0, END)
    rating_entry.delete(0, END)
    type_entry.delete(0, END)
    description_entry.delete(0, END)
