import json
import tkinter as tk
from tkinter import messagebox
from functions import MarketplaceBase

class AdminMarketplace(MarketplaceBase):
    def setup_ui(self):
        super().setup_ui()
        
        self.delete_button = tk.Button(self.frame, text="Slett", command=self.delete_existing_guide)
        self.delete_button.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
    
    def delete_existing_guide(self):
        selected_item = self.tree.selection()
        
        if not selected_item:
            messagebox.showinfo("Melding", "Vennligst velg en guide å slette.")
            return
        
        confirmation = messagebox.askokcancel("Bekreft sletting", "Er du sikker på at du vil slette valgt guide?")
        if not confirmation:
            return
        
        for item in selected_item:
            json_index = int(self.tree.item(item)["values"][0] - 1)
            del self.tours_data[json_index]
            
        self.tree.delete(*selected_item)
        self.save_data()
        
        self.listbox.delete(0, tk.END)
    
    def save_data(self):
        with open("json_files/data.json", "w") as file:
            json.dump(self.tours_data, file, indent=4)