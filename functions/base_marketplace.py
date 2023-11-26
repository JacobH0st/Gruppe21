import json
import tkinter as tk
from tkinter import VERTICAL, Listbox, Scrollbar, ttk, Button

class MarketplaceBase:
    def __init__ (self, app):
        self.app = app
        self.frame = app.marketplace_frame
        self.load_data()
        self.setup_ui()
    
    def load_data(self):
        with open('json_files/data.json', 'r') as f:
            self.tours_data = json.load(f)
    
    def setup_ui(self):
        for widget in self.frame.grid_slaves():
            widget.grid_forget()
        
        columns = ('ID', 'Hvem', 'Tidspunkt', 'Varighet', 'Tlf nr', 'Addresse', 'Pris', 'Ledige seter', 'Aldersgrense', 'Sted', 'Rating', 'Type')
        self.tree = ttk.Treeview(self.frame, columns=columns, show='headings')

        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=115)

        self.populate_treeview()

        self.listbox = Listbox(self.frame, height=15, width=55, bg="white", activestyle='dotbox', font="Helvetica", fg="black")
        self.listbox.grid(row=0, column=2)

        self.tree.bind('<<TreeviewSelect>>', self.item_selected)
        
        self.tree.grid(row=0, column=0, sticky='nsew')
        
        self.setup_scrollbars()
        
        self.back_button = Button(self.frame, text="Tilbake", command=self.app.switch_to_main_frame)
        self.back_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
        
    def populate_treeview(self):
        tours = []
        for i, tour_data in enumerate(self.tours_data, start=1):
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
        
        for tour in tours:
            self.tree.insert('', tk.END, values=tour)
            
    def setup_scrollbars(self):
        self.scrollbar_treeview = Scrollbar(self.frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar_treeview.set)
        self.scrollbar_treeview.grid(row=0, column=1, sticky='ns')

        self.scrollbar_listbox = Scrollbar(self.frame, orient=VERTICAL, command=self.listbox.yview)
        self.listbox.config(yscroll=self.scrollbar_listbox.set)
        self.scrollbar_listbox.grid(row=0, column=4, sticky='ns')
    
    def item_selected(self, event):
        for selected_item in self.tree.selection():
            self.listbox.delete(0, tk.END)
            item = self.tree.item(selected_item)

            jsonIndex = int(item['values'][0] - 1)
            company = "Hvem: " + self.tours_data[jsonIndex]['Company']
            date = "Tidspunkt: " + self.tours_data[jsonIndex]['Date and Time']
            duration = "Varighet: " + self.tours_data[jsonIndex]['Duration']
            phone = "Tlf nr: " + str(self.tours_data[jsonIndex]['Phone'])
            address = "Addresse: " + self.tours_data[jsonIndex]['Address']
            price = "Pris: " + str(self.tours_data[jsonIndex]['Price'])
            remaining_seats = "Ledige seter: " + str(self.tours_data[jsonIndex]['Available Seats']['Remaining'])
            total_seats = "Antall seter: " + str(self.tours_data[jsonIndex]['Available Seats']['Total'])
            age_limit = "Aldersgrense: " + str(self.tours_data[jsonIndex]['Age Limit'])
            place = "Sted: " + self.tours_data[jsonIndex]['Outdoor/Indoor']
            rating = "Rating: " + str(self.tours_data[jsonIndex]['Rating'])
            category = "Type: " + self.tours_data[jsonIndex]['Type']
            description = "Beskrivelse: " + self.tours_data[jsonIndex]['Description']

            self.listbox.insert(tk.END, company)
            self.listbox.insert(tk.END, date)
            self.listbox.insert(tk.END, duration)
            self.listbox.insert(tk.END, phone)
            self.listbox.insert(tk.END, address)
            self.listbox.insert(tk.END, price)
            self.listbox.insert(tk.END, remaining_seats)
            self.listbox.insert(tk.END, total_seats)
            self.listbox.insert(tk.END, age_limit)
            self.listbox.insert(tk.END, place)
            self.listbox.insert(tk.END, rating)
            self.listbox.insert(tk.END, category)
            self.listbox.insert(tk.END, description)
