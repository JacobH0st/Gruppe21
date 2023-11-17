import tkinter as tk
from tkinter import *
from tkinter import ttk
import json

with open('json_files/data.json', 'r') as f:
    tours_data = json.load(f)

def view_data_from_json(app, frame):
    frame.pack()
    
    for thingy in frame.grid_slaves():
        thingy.grid_forget()

    columns = ('ID', 'Hvem', 'Tidspunkt', 'Varighet', 'Tlf nr', 'Addresse', 'Pris', 'Ledige seter', 'Aldersgrense', 'Sted', 'Rating', 'Type')

    tree = ttk.Treeview(frame, columns=columns, show='headings')

    for column in columns:
        tree.heading(column, text=column)
        tree.column(column, width=115)

    tours = []
    for i, tour_data in enumerate(tours_data, start=1):
        id = i
        company = tour_data['Company']
        date = tour_data['Date and Time']
        duration = tour_data['Duration']
        phone = tour_data['Phone']
        address = tour_data['Address']
        price = tour_data['Price']
        remaining_seats = tour_data['Available Seats']['Remaining']
        total_seats = tour_data['Available Seats']['Total']
        age_limit = tour_data['Age Limit']
        place = tour_data['Outdoor/Indoor']
        rating = tour_data['Rating']
        category = tour_data['Type']
        description = tour_data['Description']

        tours.append((id, company, date, duration, phone, address, price, f"{remaining_seats}/{total_seats}", age_limit, place, rating, category, description))

    # Add data to the Treeview
    for tour in tours:
        tree.insert('', tk.END, values=tour)

    listbox = Listbox(frame, height=15, width=55, bg="white", activestyle='dotbox', font="Helvetica", fg="black")
    listbox.grid(row=0, column=2)

    def item_selected(event):
        for selected_item in tree.selection():
            listbox.delete(0, END)
            item = tree.item(selected_item)

            jsonIndex = item['values'][0] - 1
            company = "Hvem: " + tours_data[jsonIndex]['Company']
            date = "Tidspunkt: " + tours_data[jsonIndex]['Date and Time']
            duration = "Varighet: " + tours_data[jsonIndex]['Duration']
            phone = "Tlf nr: " + str(tours_data[jsonIndex]['Phone'])
            address = "Addresse: " + tours_data[jsonIndex]['Address']
            price = "Pris: " + str(tours_data[jsonIndex]['Price'])
            remaining_seats = "Ledige seter: " + str(tours_data[jsonIndex]['Available Seats']['Remaining'])
            total_seats = "Antall seter: " + str(tours_data[jsonIndex]['Available Seats']['Total'])
            age_limit = "Aldersgrense: " + str(tours_data[jsonIndex]['Age Limit'])
            place = "Sted: " + tours_data[jsonIndex]['Outdoor/Indoor']
            rating = "Rating: " + str(tours_data[jsonIndex]['Rating'])
            category = "Type: " + tours_data[jsonIndex]['Type']
            description = "Beskrivelse: " + tours_data[jsonIndex]['Description']

            listbox.insert(END, company)
            listbox.insert(END, date)
            listbox.insert(END, duration)
            listbox.insert(END, phone)
            listbox.insert(END, address)
            listbox.insert(END, price)
            listbox.insert(END, remaining_seats)
            listbox.insert(END, total_seats)
            listbox.insert(END, age_limit)
            listbox.insert(END, place)
            listbox.insert(END, rating)
            listbox.insert(END, category)
            listbox.insert(END, description)


    tree.bind('<<TreeviewSelect>>', item_selected)

    tree.grid(row=0, column=0, sticky='nsew')

    # SCROLLBAR
    scrollbar_treeview = Scrollbar(frame, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar_treeview.set)
    scrollbar_treeview.grid(row=0, column=1, sticky='ns')

    scrollbar_listbox = Scrollbar(frame, orient=VERTICAL, command=listbox.yview)
    listbox.config(yscroll=scrollbar_listbox.set)
    scrollbar_listbox.grid(row=0, column=4, sticky='ns')
    
    back_button = tk.Button(frame, text="Tilbake", command=app.switch_to_main_frame)
    back_button.grid(row=15, column=0, columnspan=2, padx=10, pady=10)
    
    # TODO FIKS BESTILL LOGIKK, OPPDATERE ANTALL PLASSER
    
    reserve_button = Button(frame, text="Bestill", command={})
    reserve_button.grid(row=15, column=2, columnspan=1, padx=10, pady=10)
