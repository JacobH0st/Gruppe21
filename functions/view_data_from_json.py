import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json

def view_data_from_json():
    window = tk.Toplevel()
    window.title('Marketplace')
    

    columns = (
        'Company', 'Date and Time', 'Duration', 'Phone', 'Address', 'Price',
        'Remaining Seats', 'Age Limit', 'Outdoor/Indoor', 'Rating', 'Type', 'Description'
    )

    tree = ttk.Treeview(window, columns=columns, show='headings')

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    with open('json_files/data.json', 'r') as file:
        data = json.load(file)

    for item in data:
        company = item.get('Company', '')
        datetime = item.get('Date and Time', '')
        duration = item.get('Duration', '')
        phone = item.get('Phone', '')
        address = item.get('Address', '')
        price = item.get('Price', '')
        remaining_seats = item.get('Available Seats', {}).get('Remaining', '')
        age_limit = item.get('Age Limit', '')
        outdoor_indoor = item.get('Outdoor/Indoor', '')
        rating = item.get('Rating', '')
        type = item.get('Type', '')
        description = item.get('Description', '')

        tree.insert('', tk.END, values=(
            company, datetime, duration, phone, address, price,
            remaining_seats, age_limit, outdoor_indoor, rating, type, description
        ))

    tree.pack(fill='both', expand=True)

    def item_selected(event):
        selected_item = tree.selection()[0]
        item = tree.item(selected_item)
        record = item['values']
        showinfo(title='Information', message='\n'.join(f'{columns[i]}: {record[i]}' for i in range(len(columns))))

    tree.bind('<<TreeviewSelect>>', item_selected)
