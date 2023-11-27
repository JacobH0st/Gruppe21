import tkinter as tk
from tkinter import messagebox
from functions import MarketplaceBase

class UserMarketplace(MarketplaceBase):
    def setup_ui(self):
        super().setup_ui()
        
        self.reserve_button = tk.Button(self.frame, text="Bestill", command=self.reserve)
        self.reserve_button.grid(row=1, column=2, columnspan=1, padx=10, pady=10)
    
    def reserve(self):
        #TODO: legg til reservasjon oppdateringer, f.eks. antall ledige plasser oppdateres og legg til en knapp for avbestilling.
        messagebox.showinfo("Kommer", "Ikke implementert enda")